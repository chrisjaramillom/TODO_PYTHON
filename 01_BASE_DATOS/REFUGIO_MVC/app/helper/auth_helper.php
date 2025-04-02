<?php
function verificarRol($rolesPermitidos = [])
{
    if (!isset($_SESSION['usuario'])) {
        header("Location: /refugio_mvc/public/auth/login");
        exit();
    }

    if (!in_array($_SESSION['usuario']['rol'], $rolesPermitidos)) {
        echo "<h2>⛔ Acceso denegado. No tienes permisos suficientes.</h2>";
        exit();
    }
}
