<?php
require_once "../app/config/database.php";

class Estadistica
{
    private $conn;

    public function __construct()
    {
        $db = new Database();
        $this->conn = $db->connect();
    }

    public function getAnimalesMasAtendidos()
    {
        $sql = "SELECT * FROM vista_animales_mas_atendidos";
        $stmt = $this->conn->prepare($sql);
        $stmt->execute();
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }
}
