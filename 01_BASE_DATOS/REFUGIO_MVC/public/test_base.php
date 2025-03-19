<?php
require_once "../app/config/database.php";
$db = new Database();
$conn = $db->connect();

if ($conn) {
    echo "✅ Conexión exitosa a la base de datos.";
} else {
    echo "❌ Error en la conexión.";
}
