<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <title>Animales Más Atendidos</title>
    <link rel="stylesheet" href="/refugio_mvc/public/css/styles.css">
</head>

<body>
    <h1>🐾 Animales Más Atendidos</h1>

    <table border="1" cellpadding="10">
        <thead>
            <tr>
                <th>ID</th>
                <th>Nombre</th>
                <th>Especie</th>
                <th>Total de Atenciones</th>
            </tr>
        </thead>
        <tbody>
            <?php foreach ($data as $animal): ?>
                <tr>
                    <td><?= $animal['ani_id'] ?></td>
                    <td><?= $animal['ani_nombre'] ?></td>
                    <td><?= $animal['ani_especie'] ?></td>
                    <td><?= $animal['total_atenciones'] ?></td>
                </tr>
            <?php endforeach; ?>
        </tbody>
    </table>

    <br>
    <a href="/refugio_mvc/public/animal/index">🔙 Volver</a>
</body>

</html>