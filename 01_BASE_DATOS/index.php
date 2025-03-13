<?php
// Inicializar variables
$mensaje = '';
$error = '';
$departamentoEditar = null;

// Función para ejecutar comandos Python
function ejecutarPython($comando)
{
    $resultado = shell_exec('python ' . $comando);
    return json_decode($resultado, true);
}

// Procesar formularios
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    if (isset($_POST['accion'])) {
        $nombre = $_POST['nombre'] ?? '';
        $ubicacion = $_POST['ubicacion'] ?? '';
        $bandera = isset($_POST['bandera']) ? 1 : 0;

        // Crear departamento
        if ($_POST['accion'] === 'crear') {
            $cmd = "python_scripts/crear_departamento.py \"$nombre\" \"$ubicacion\" $bandera";
            $resultado = ejecutarPython($cmd);

            if ($resultado['success']) {
                $mensaje = "Departamento creado con éxito";
            } else {
                $error = "Error al crear departamento";
            }
        }
        // Actualizar departamento
        else if ($_POST['accion'] === 'actualizar' && isset($_POST['id'])) {
            $id = $_POST['id'];
            $cmd = "python_scripts/actualizar_departamento.py $id \"$nombre\" \"$ubicacion\" $bandera";
            $resultado = ejecutarPython($cmd);

            if ($resultado['success']) {
                $mensaje = "Departamento actualizado con éxito";
            } else {
                $error = "Error al actualizar departamento";
            }
        }
    }
    // Eliminar departamento
    else if (isset($_POST['eliminar']) && isset($_POST['id'])) {
        $id = $_POST['id'];
        $cmd = "python_scripts/eliminar_departamento.py $id";
        $resultado = ejecutarPython($cmd);

        if ($resultado['success']) {
            $mensaje = "Departamento eliminado con éxito";
        } else {
            $error = "Error al eliminar departamento";
        }
    }
}

// Comprobar si se solicita editar
if (isset($_GET['editar'])) {
    $id = $_GET['editar'];
    $cmd = "python_scripts/obtener_departamento.py $id";
    $resultado = ejecutarPython($cmd);

    if ($resultado['success']) {
        $departamentoEditar = $resultado['data'];
    }
}

// Obtener todos los departamentos
$cmd = "python_scripts/obtener_departamentos.py";
$resultado = ejecutarPython($cmd);
$departamentos = $resultado['success'] ? $resultado['data'] : [];
?>

<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gestión de Departamentos</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
        }

        .container {
            max-width: 1000px;
            margin: 0 auto;
        }

        .mensaje {
            background-color: #d4edda;
            color: #155724;
            padding: 10px;
            margin-bottom: 15px;
            border-radius: 4px;
        }

        .error {
            background-color: #f8d7da;
            color: #721c24;
            padding: 10px;
            margin-bottom: 15px;
            border-radius: 4px;
        }

        form {
            background-color: #f5f5f5;
            padding: 15px;
            border-radius: 4px;
            margin-bottom: 20px;
        }

        .form-group {
            margin-bottom: 10px;
        }

        label {
            display: block;
            margin-bottom: 5px;
        }

        input[type="text"] {
            width: 100%;
            padding: 8px;
            box-sizing: border-box;
        }

        input[type="checkbox"] {
            margin-right: 5px;
        }

        button {
            background-color: #007bff;
            color: white;
            border: none;
            padding: 10px 15px;
            cursor: pointer;
            border-radius: 4px;
        }

        button:hover {
            background-color: #0069d9;
        }

        table {
            width: 100%;
            border-collapse: collapse;
        }

        th,
        td {
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }

        th {
            background-color: #f2f2f2;
        }

        tr:nth-child(even) {
            background-color: #f9f9f9;
        }

        .acciones {
            display: flex;
            gap: 5px;
        }

        .btn-editar {
            background-color: #ffc107;
        }

        .btn-eliminar {
            background-color: #dc3545;
        }

        h2 {
            margin-top: 0;
            color: #444;
        }
    </style>
</head>

<body>
    <div class="container">
        <h1>Gestión de Departamentos</h1>

        <?php if ($mensaje): ?>
            <div class="mensaje"><?php echo $mensaje; ?></div>
        <?php endif; ?>

        <?php if ($error): ?>
            <div class="error"><?php echo $error; ?></div>
        <?php endif; ?>

        <!-- Formulario para crear o actualizar departamento -->
        <form method="POST" action="">
            <h2><?php echo $departamentoEditar ? 'Editar Departamento' : 'Nuevo Departamento'; ?></h2>

            <?php if ($departamentoEditar): ?>
                <input type="hidden" name="id" value="<?php echo $departamentoEditar['DEP_ID']; ?>">
                <input type="hidden" name="accion" value="actualizar">
            <?php else: ?>
                <input type="hidden" name="accion" value="crear">
            <?php endif; ?>

            <div class="form-group">
                <label for="nombre">Nombre:</label>
                <input type="text" id="nombre" name="nombre" required
                    value="<?php echo $departamentoEditar ? $departamentoEditar['DEP_NOMBRE'] : ''; ?>">
            </div>

            <div class="form-group">
                <label for="ubicacion">Ubicación:</label>
                <input type="text" id="ubicacion" name="ubicacion" required
                    value="<?php echo $departamentoEditar ? $departamentoEditar['DEP_UBICA'] : ''; ?>">
            </div>

            <div class="form-group">
                <label>
                    <input type="checkbox" name="bandera"
                        <?php echo (!$departamentoEditar || $departamentoEditar['DEP_BANDERA'] == 1) ? 'checked' : ''; ?>>
                    Activo
                </label>
            </div>

            <button type="submit"><?php echo $departamentoEditar ? 'Actualizar' : 'Crear'; ?> Departamento</button>

            <?php if ($departamentoEditar): ?>
                <a href="index.php" style="margin-left: 10px;">Cancelar</a>
            <?php endif; ?>
        </form>

        <!-- Tabla de departamentos -->
        <h2>Lista de Departamentos</h2>
        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nombre</th>
                    <th>Ubicación</th>
                    <th>Estado</th>
                    <th>Acciones</th>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($departamentos as $depto): ?>
                    <tr>
                        <td><?php echo $depto['DEP_ID']; ?></td>
                        <td><?php echo $depto['DEP_NOMBRE']; ?></td>
                        <td><?php echo $depto['DEP_UBICA']; ?></td>
                        <td><?php echo $depto['DEP_BANDERA'] == 1 ? 'Activo' : 'Inactivo'; ?></td>
                        <td class="acciones">
                            <a href="?editar=<?php echo $depto['DEP_ID']; ?>">
                                <button class="btn-editar">Editar</button>
                            </a>
                            <form method="POST" action="" style="display:inline;"
                                onsubmit="return confirm('¿Estás seguro de eliminar este departamento?');">
                                <input type="hidden" name="id" value="<?php echo $depto['DEP_ID']; ?>">
                                <button type="submit" name="eliminar" class="btn-eliminar">Eliminar</button>
                            </form>
                        </td>
                    </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
    </div>
</body>

</html>