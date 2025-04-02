<?php require_once "../app/views/partials/menu.php"; ?>

<?php if (!empty($_SESSION['error'])): ?>
    <div class="alert alert-danger">
        <?= $_SESSION['error'];
        unset($_SESSION['error']); ?>
    </div>
<?php endif; ?>


<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <title>Nuevo Usuario</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>

<body class="bg-light">
    <div class="container py-4">
        <h2 class="text-center mb-4">Crear Nuevo Usuario</h2>

        <form action="/refugio_mvc/public/usuario/store" method="POST" class="card p-4 shadow">
            <?php if (!empty($_SESSION['error'])): ?>
                <div class="alert alert-danger">
                    <?= $_SESSION['error'];
                    unset($_SESSION['error']); ?>
                </div>
            <?php endif; ?>

            <div class="mb-3">
                <label>Nombre completo</label>
                <input type="text" name="nombre" class="form-control" required>
            </div>

            <div class="mb-3">
                <label>Correo electrónico</label>
                <input type="email" name="email" class="form-control" required>
            </div>

            <div class="mb-3">
                <label>Contraseña</label>
                <input type="password" name="password" class="form-control" required>
            </div>

            <div class="mb-3">
                <label>Rol de usuario</label>
                <select name="rol" class="form-select" required>
                    <option value="">-- Seleccione un rol --</option>
                    <option value="Cuidador">Cuidador</option>
                    <option value="Doctor">Doctor</option>
                    <option value="Administrador">Administrador</option>
                </select>
            </div>

            <div class="text-center">
                <button type="submit" class="btn btn-success">Registrar Usuario</button>
                <a href="/refugio_mvc/public/usuario/index" class="btn btn-secondary ms-2">Cancelar</a>
            </div>
        </form>
    </div>
</body>

</html>