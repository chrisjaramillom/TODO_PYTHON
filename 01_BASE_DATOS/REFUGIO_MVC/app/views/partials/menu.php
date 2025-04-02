<?php
session_start();
$usuario = $_SESSION['usuario'] ?? null;
?>

<div style="background-color: #4CAF50; padding: 15px; color: white;">
    <strong>Refugio Municipal</strong>
    <?php if ($usuario): ?>
        <span style="margin-left: 30px;">👤 <?= $usuario['nombre'] ?> (<?= $usuario['rol'] ?>)</span>
        <span style="float: right;"><a href="/refugio_mvc/public/auth/logout" style="color:white;">Cerrar sesión</a></span>
        <br><br>

        <?php if ($usuario['rol'] === 'Administrador' || $usuario['rol'] === 'Cuidador'): ?>
            <a href="/refugio_mvc/public/animal/index" style="color:white; margin-right:15px;">🐾 Animales</a>
        <?php endif; ?>

        <?php if ($usuario['rol'] === 'Administrador' || $usuario['rol'] === 'Doctor'): ?>
            <a href="/refugio_mvc/public/atencionmedica/index" style="color:white; margin-right:15px;">🩺 Atención Médica</a>
        <?php endif; ?>

        <?php if ($usuario['rol'] === 'Administrador'): ?>
            <a href="/refugio_mvc/public/usuario/index" style="color:white;">👥 Usuarios</a>
        <?php endif; ?>
    <?php else: ?>
        <span style="float: right;"><a href="/refugio_mvc/public/auth/login" style="color:white;">Iniciar sesión</a></span>
    <?php endif; ?>
</div>