<?php require_once "../app/views/partials/menu.php"; ?>

<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <title>Diagnósticos</title>
    <link rel="stylesheet" href="/refugio_mvc/public/css/styles.css">
</head>

<body>
    <h1>Diagnósticos de la Atención Médica</h1>

    <div style="text-align: center; margin-bottom: 20px;">
        <a href="/refugio_mvc/public/diagnostico/store/<?= $_GET['atm_id'] ?? 1 ?>">
            <button>+ Nuevo Diagnóstico</button>
        </a>
    </div>

    <table>
        <thead>
            <tr>
                <th>ID</th>
                <th>Enfermedad</th>
                <th>Síntomas</th>
                <th>Tratamiento</th>
                <th>Medicamentos / Indicaciones</th>
                <th>Acciones</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($diagnosticos as $diag): ?>
                <tr>
                    <td><?= $diag['diag_id'] ?></td>
                    <td><?= $diag['diag_enfermedad'] ?></td>
                    <td><?= $diag['diag_sintomas'] ?></td>
                    <td><?= $diag['diag_tratamiento'] ?></td>
                    <td><?= $diag['diag_medicamentos'] ?></td>
                    <td>
                        <a href="/refugio_mvc/public/diagnostico/delete/<?= $diag['diag_id'] ?>" onclick="return confirm('¿Eliminar diagnóstico?')">Eliminar</a>
                    </td>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>

    <div style="text-align: center; margin-top: 20px;">
        <a href="/refugio_mvc/public/atencionmedica/index">⬅ Volver al listado de atenciones</a>
    </div>
</body>

</html>