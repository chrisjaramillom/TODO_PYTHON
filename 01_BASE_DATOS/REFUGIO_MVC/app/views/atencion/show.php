<?php require_once "../app/views/partials/menu.php"; ?>

<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <title>Detalle de Atención Médica</title>
    <link rel="stylesheet" href="/refugio_mvc/public/css/styles.css">
</head>

<body>
    <h1>Detalle de Atención Médica</h1>

    <?php if ($atencion): ?>
        <p><strong>ID:</strong> <?= $atencion['atm_id'] ?></p>
        <p><strong>Motivo:</strong> <?= $atencion['atm_motivo'] ?></p>
        <p><strong>Detalles:</strong> <?= $atencion['atm_detalles'] ?></p>
        <p><strong>ID Animal:</strong> <?= $atencion['ani_id'] ?></p>
        <p><strong>ID Doctor:</strong> <?= $atencion['doc_id'] ?></p>
        <p><strong>Fecha:</strong> <?= $atencion['atm_fecha_atencion'] ?></p>
    <?php else: ?>
        <p>No se encontró la atención médica.</p>
    <?php endif; ?>

    <div style="margin-top: 20px;">
        <a href="/refugio_mvc/public/atencionmedica/index">Volver al listado</a>
    </div>
</body>

</html>