<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <title>Registrar Nuevo Animal</title>
    <link rel="stylesheet" href="/refugio_mvc/public/css/styles.css">
</head>

<body>
    <h1>Registrar Nuevo Animal</h1>

    <form action="/refugio_mvc/public/animal/store" method="POST">
        <div><label>Nombre:</label><input type="text" name="nombre" required></div><br>
        <div><label>Especie:</label>
            <select name="especie" required>
                <option value="Canino">Canino</option>
                <option value="Felino">Felino</option>
                <option value="Ovino">Ovino</option>
                <option value="Bovino">Bovino</option>
                <option value="Caprino">Caprino</option>
                <option value="Porcino">Porcino</option>
                <option value="Leporino">Leporino</option>
                <option value="Equino">Equino</option>
            </select>
        </div><br>
        <div><label>Tipo:</label><input type="text" name="tipo" required></div><br>
        <div><label>Raza:</label><input type="text" name="raza" required></div><br>
        <div><label>Fecha de Ingreso:</label><input type="date" name="fecha_ingreso" required></div><br>
        <div><label>Lugar de Recogida:</label><input type="text" name="lugar_recogida" required></div><br>
        <div><label>Sexo:</label>
            <select name="sexo" required>
                <option value="Macho">Macho</option>
                <option value="Hembra">Hembra</option>
            </select>
        </div><br>
        <div><label>ID del Cuidador:</label><input type="number" name="cui_id" required></div><br>

        <div style="text-align:center;"><button type="submit">Registrar</button></div>
    </form>

    <div style="text-align:center;">
        <a href="/refugio_mvc/public/animal/index">Volver a la lista</a>
    </div>
</body>

</html>