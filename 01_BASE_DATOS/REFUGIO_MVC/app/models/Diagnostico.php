<?php
require_once "../app/config/database.php";

class Diagnostico
{
    private $conn;

    public function __construct()
    {
        $db = new Database();
        $this->conn = $db->connect();
    }

    public function getByAtencion($atm_id)
    {
        $sql = "SELECT * FROM Diagnostico WHERE atm_id = :atm_id AND diag_estado = TRUE";
        $stmt = $this->conn->prepare($sql);
        $stmt->bindParam(':atm_id', $atm_id);
        $stmt->execute();
        return $stmt->fetchAll();
    }

    public function getById($id)
    {
        $sql = "SELECT * FROM Diagnostico WHERE diag_id = :id";
        $stmt = $this->conn->prepare($sql);
        $stmt->bindParam(':id', $id);
        $stmt->execute();
        return $stmt->fetch();
    }

    public function create($atm_id, $enfermedad, $sintomas, $tratamiento, $medicamentos)
    {
        $sql = "INSERT INTO Diagnostico (atm_id, diag_enfermedad, diag_sintomas, diag_tratamiento, diag_medicamentos, diag_estado)
                VALUES (:atm_id, :enfermedad, :sintomas, :tratamiento, :medicamentos, TRUE)";
        $stmt = $this->conn->prepare($sql);
        $stmt->bindParam(':atm_id', $atm_id);
        $stmt->bindParam(':enfermedad', $enfermedad);
        $stmt->bindParam(':sintomas', $sintomas);
        $stmt->bindParam(':tratamiento', $tratamiento);
        $stmt->bindParam(':medicamentos', $medicamentos);
        return $stmt->execute();
    }

    public function delete($id)
    {
        $sql = "UPDATE Diagnostico SET diag_estado = FALSE WHERE diag_id = :id";
        $stmt = $this->conn->prepare($sql);
        $stmt->bindParam(':id', $id);
        return $stmt->execute();
    }

    public function getAll()
    {
        $sql = "SELECT * FROM Diagnostico WHERE diag_estado = 1";
        $stmt = $this->conn->prepare($sql);
        $stmt->execute();
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }
}
