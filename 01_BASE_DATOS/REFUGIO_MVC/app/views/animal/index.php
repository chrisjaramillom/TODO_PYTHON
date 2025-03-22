<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <title>Lista de Animales</title>
    <link rel="stylesheet" href="/refugio_mvc/public/css/styles.css">
</head>

<body>
    <h1>Lista de Animales</h1>

    <div style="text-align: center; margin-bottom: 20px;">
        <a href="/refugio_mvc/public/animal/store">
            <button>+ Nuevo Animal</button>
        </a>
    </div>

    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Nombre</th>
                <th>Especie</th>
                <th>Raza</th>
                <th>Fecha de Ingreso</th>
                <th>Acciones</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($animales as $animal): ?>
                <tr>
                    <td><?= $animal['ani_id'] ?></td>
                    <td><?= $animal['ani_nombre'] ?></td>
                    <td><?= $animal['ani_especie'] ?></td>
                    <td><?= $animal['ani_raza'] ?></td>
                    <td><?= $animal['ani_fecha_ingreso'] ?></td>
                    <td>
                        <a href="/refugio_mvc/public/animal/show/<?= $animal['ani_id'] ?>">Ver</a> |
                        <a href="/refugio_mvc/public/animal/delete/<?= $animal['ani_id'] ?>" onclick="return confirm('¿Seguro que deseas eliminar este registro?')">Eliminar</a>
                    </td>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>
</body>

</html>