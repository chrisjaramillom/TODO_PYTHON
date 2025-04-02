<?php require_once "../app/views/partials/menu.php"; ?>

<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <title>Usuarios del Sistema</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>

<body class="bg-light">
    <div class="container py-4">
        <h2 class="text-center mb-4">Lista de Usuarios</h2>

        <div class="text-end mb-3">
            <a href="/refugio_mvc/public/usuario/create" class="btn btn-primary">+ Nuevo Usuario</a>
        </div>

        <table class="table table-striped table-hover table-bordered">
            <thead class="table-dark text-center">
                <tr>
                    <th>ID</th>
                    <th>Nombre</th>
                    <th>Email</th>
                    <th>Rol</th>
                    <th>Estado</th>
                    <th>Acciones</th>
                </tr>
            </thead>
            <tbody>
                <?php foreach ($usuarios as $usuario): ?>
                    <tr>
                        <td class="text-center"><?= $usuario['usr_id'] ?></td>
                        <td><?= $usuario['usr_nombre'] ?></td>
                        <td><?= $usuario['usr_email'] ?></td>
                        <td><?= $usuario['usr_rol'] ?></td>
                        <td class="text-center">
                            <?= $usuario['usr_estado'] ? 'Activo' : 'Inactivo' ?>
                        </td>
                        <td class="text-center">
                            <?php if ($usuario['usr_estado']): ?>
                                <a href="/refugio_mvc/public/usuario/delete/<?= $usuario['usr_id'] ?>" class="btn btn-sm btn-danger"
                                    onclick="return confirm('¿Estás seguro de desactivar este usuario?')">
                                    Desactivar
                                </a>
                            <?php else: ?>
                                <em>--</em>
                            <?php endif; ?>
                        </td>
                    </tr>
                <?php endforeach; ?>
            </tbody>
        </table>
    </div>
</body>

</html>