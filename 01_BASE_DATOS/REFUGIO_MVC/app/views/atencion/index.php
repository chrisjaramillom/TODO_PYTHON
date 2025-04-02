<?php require_once "../app/views/partials/menu.php"; ?>

<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <title>Lista de Atenciones Médicas</title>
    <link rel="stylesheet" href="/refugio_mvc/public/css/styles.css">
</head>

<body>
    <h1>Lista de Atenciones Médicas</h1>

    <div style="text-align: center; margin-bottom: 20px;">
        <a href="/refugio_mvc/public/atencionmedica/store">
            <button>+ Nueva Atención</button>
        </a>
    </div>

    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Animal</th>
                <th>Doctor</th>
                <th>Motivo</th>
                <th>Fecha</th>
                <th>Acciones</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($atenciones as $atencion): ?>
                <tr>
                    <td><?= $atencion['atm_id'] ?></td>
                    <td><?= $atencion['ani_nombre'] ?></td>
                    <td><?= $atencion['doc_nombre'] ?></td>
                    <td><?= $atencion['atm_motivo'] ?></td>
                    <td><?= $atencion['atm_fecha_atencion'] ?></td>
                    <td>
                        <a href="/refugio_mvc/public/atencionmedica/show/<?= $atencion['atm_id'] ?>">Ver</a> |
                        <a href="/refugio_mvc/public/atencionmedica/delete/<?= $atencion['atm_id'] ?>" onclick="return confirm('¿Eliminar atención?')">Eliminar</a>
                    </td>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>
</body>

</html>