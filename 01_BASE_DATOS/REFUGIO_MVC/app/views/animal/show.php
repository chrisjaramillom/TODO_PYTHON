<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Detalles del Animal</title>
    <link rel="stylesheet" href="/refugio_mvc/public/css/styles.css">
</head>

<body>
    <h1>Detalles del Animal</h1>
    <?php if ($animal): ?>
        <p><strong>ID:</strong> <?= $animal['ani_id'] ?></p>
        <p><strong>Nombre:</strong> <?= $animal['ani_nombre'] ?></p>
        <p><strong>Especie:</strong> <?= $animal['ani_especie'] ?></p>
        <p><strong>Tipo:</strong> <?= $animal['ani_tipo'] ?></p>
        <p><strong>Raza:</strong> <?= $animal['ani_raza'] ?></p>
        <p><strong>Fecha de Ingreso:</strong> <?= $animal['ani_fecha_ingreso'] ?></p>
        <p><strong>Lugar de Recogida:</strong> <?= $animal['ani_lugar_recogida'] ?></p>
        <p><strong>Sexo:</strong> <?= $animal['ani_sexo'] ?></p>
    <?php else: ?>
        <p>No se encontró información del animal.</p>
    <?php endif; ?>
    <a href="/refugio_mvc/public/animal/index">Volver a la lista</a>
</body>

</html>