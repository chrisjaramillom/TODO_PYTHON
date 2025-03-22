<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <title>Login - Refugio</title>
    <link rel="stylesheet" href="/refugio_mvc/public/css/styles.css">
</head>

<body>
    <h1>Ingreso al Sistema</h1>
    <?php
    if (isset($_SESSION['error'])): ?>
        <p style="color: red"><?= $_SESSION['error'];
                                unset($_SESSION['error']); ?></p>
    <?php endif; ?>
    <form action="/refugio_mvc/public/auth/acceder" method="POST">
        <label>Correo electrónico:</label><br>
        <input type="email" name="email" required><br><br>
        <label>Contraseña:</label><br>
        <input type="password" name="password" required><br><br>
        <button type="submit">Ingresar</button>
    </form>
</body>

</html>