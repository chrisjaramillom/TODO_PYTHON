<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Detalles del Animal</title>
    <link rel="stylesheet" href="/refugio_mvc/public/css/styles.css">
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f2f2f2;
            margin: 20px;
        }

        .card {
            background-color: white;
            max-width: 600px;
            margin: auto;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }

        h1 {
            text-align: center;
            color: #2e7d32;
        }

        .detail-row {
            margin: 10px 0;
        }

        .detail-row strong {
            color: #333;
            width: 180px;
            display: inline-block;
        }

        .btn-back {
            display: block;
            text-align: center;
            margin-top: 30px;
        }

        .btn-back a {
            background-color: #4CAF50;
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            border-radius: 6px;
            transition: background-color 0.3s;
        }

        .btn-back a:hover {
            background-color: #45a049;
        }
    </style>
</head>

<body>

    <div class="card">
        <h1>🐾 Detalles del Animal</h1>

        <?php if ($animal): ?>
            <div class="detail-row"><strong>ID:</strong> <?= $animal['ani_id'] ?></div>
            <div class="detail-row"><strong>Nombre:</strong> <?= $animal['ani_nombre'] ?></div>
            <div class="detail-row"><strong>Especie:</strong> <?= $animal['ani_especie'] ?></div>
            <div class="detail-row"><strong>Tipo:</strong> <?= $animal['ani_tipo'] ?></div>
            <div class="detail-row"><strong>Raza:</strong> <?= $animal['ani_raza'] ?></div>
            <div class="detail-row"><strong>Fecha de Ingreso:</strong> <?= $animal['ani_fecha_ingreso'] ?></div>
            <div class="detail-row"><strong>Lugar de Recogida:</strong> <?= $animal['ani_lugar_recogida'] ?></div>
            <div class="detail-row"><strong>Sexo:</strong> <?= $animal['ani_sexo'] ?></div>
        <?php else: ?>
            <p>No se encontró información del animal.</p>
        <?php endif; ?>

        <div class="btn-back">
            <a href="/refugio_mvc/public/animal/index">← Volver a la Lista</a>
        </div>
    </div>

</body>

</html>