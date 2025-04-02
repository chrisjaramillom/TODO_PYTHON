<?php
require_once "../app/config/database.php";

class Doctor
{
    private $conn;

    public function __construct()
    {
        $db = new Database();
        $this->conn = $db->connect();
    }

    public function getAll()
    {
        $stmt = $this->conn->query("SELECT doc_id, doc_nombre FROM Doctor WHERE doc_estado = 1");
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }
}
