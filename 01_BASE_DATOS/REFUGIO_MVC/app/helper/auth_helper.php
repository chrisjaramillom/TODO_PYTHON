<?php
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}

function verificarPermisos($modulo, $rolesPermitidos)
{
    if (!isset($_SESSION['usuario'])) {
        header("Location: /refugio_mvc/public/auth/login");
        exit();
    }

    $rol = $_SESSION['usuario']['rol'];

    if (!in_array($rol, $rolesPermitidos)) {
        echo '<h2 style="color: red; text-align: center;">⛔ Acceso denegado al módulo <strong>' . $modulo . '</strong>. No tienes permisos suficientes.</h2>';
        exit();
    }
}
