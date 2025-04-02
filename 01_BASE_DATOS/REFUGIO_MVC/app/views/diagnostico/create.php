<?php require_once "../app/views/partials/menu.php"; ?>

<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <title>Nuevo Diagnóstico</title>
    <link rel="stylesheet" href="/refugio_mvc/public/css/styles.css">
</head>

<body>
    <h1>Registrar Diagnóstico</h1>

    <form action="/refugio_mvc/public/diagnostico/store/<?= $_GET['atm_id'] ?? 1 ?>" method="POST" style="max-width: 600px; margin: auto;">
        <div>
            <label>Enfermedad:</label>
            <input type="text" name="enfermedad" required>
        </div><br>

        <div>
            <label>Síntomas:</label>
            <textarea name="sintomas" rows="3" required></textarea>
        </div><br>

        <div>
            <label>Tratamiento:</label>
            <textarea name="tratamiento" rows="3" required></textarea>
        </div><br>

        <div>
            <label>Medicamentos e Indicaciones:</label>
            <textarea name="medicamentos" rows="3" required></textarea>
        </div><br>

        <div style="text-align: center;">
            <button type="submit">Registrar</button>
        </div>
    </form>

    <div style="text-align: center; margin-top: 20px;">
        <a href="/refugio_mvc/public/diagnostico/index/<?= $_GET['atm_id'] ?? 1 ?>">⬅ Volver</a>
    </div>
</body>

</html>