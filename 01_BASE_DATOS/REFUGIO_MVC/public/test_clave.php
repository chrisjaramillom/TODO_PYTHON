<?php
$claveIngresada = "12345"; // La que estás escribiendo en el login
$hashGuardado = '$2y$10$dHIO8nEDEFDkxyHvBqN0m.7IFCk5BUqFlQKjPPSda1jWUitcVG/OS';
if (password_verify($claveIngresada, $hashGuardado)) {
    echo "✅ La contraseña es correcta.";
} else {
    echo "❌ Contraseña incorrecta.";
}
