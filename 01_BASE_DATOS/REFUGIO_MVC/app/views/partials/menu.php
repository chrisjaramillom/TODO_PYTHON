<?php
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}

$usuario = $_SESSION['usuario'] ?? null;
?>

<div style="background-color: #4CAF50; padding: 15px; color: white;">
    <strong>Refugio Municipal</strong>

    <?php if ($usuario): ?>
        <span style="margin-left: 30px;">👤 <?= htmlspecialchars($usuario['nombre'] ?? ''); ?> (<?= htmlspecialchars($usuario['rol'] ?? ''); ?>)</span>
        <span style="float: right;"><a href="/refugio_mvc/public/auth/logout" style="color:white;">Cerrar sesión</a></span>
        <br><br>

        <?php if (in_array($usuario['rol'], ['Administrador', 'Cuidador', 'Médico'])): ?>
            <a href="/refugio_mvc/public/animal/index" style="color:white; margin-right:15px;">🐾 Animales</a>
        <?php endif; ?>

        <?php if (in_array($usuario['rol'], ['Administrador', 'Médico'])): ?>
            <a href="/refugio_mvc/public/atencionmedica/index" style="color:white; margin-right:15px;">🩺 Atención Médica</a>
        <?php endif; ?>

        <?php if ($usuario['rol'] === 'Médico'): ?>
            <a href="/refugio_mvc/public/estadisticas/animalesMasAtendidos" style="color:white; margin-right:15px;">📊 Más Atendidos</a>
        <?php endif; ?>

        <?php if ($usuario['rol'] === 'Administrador'): ?>
            <a href="/refugio_mvc/public/usuario/index" style="color:white;">👥 Usuarios</a>
        <?php endif; ?>

    <?php else: ?>
        <span style="float: right;"><a href="/refugio_mvc/public/auth/login" style="color:white;">Iniciar sesión</a></span>
    <?php endif; ?>
</div>