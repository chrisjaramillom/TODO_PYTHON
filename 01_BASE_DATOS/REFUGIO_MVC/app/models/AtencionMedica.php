<?php
require_once "../app/config/database.php";

class AtencionMedica
{
    private $conn;

    public function __construct()
    {
        $db = new Database();
        $this->conn = $db->connect();
    }

    public function getAll()
    {
        $sql = "SELECT atm.*, ani.ani_nombre, doc.doc_nombre 
                FROM Atencion_Medica atm
                JOIN Animal ani ON ani.ani_id = atm.ani_id
                JOIN Doctor doc ON doc.doc_id = atm.doc_id
                WHERE atm.atm_estado = TRUE";
        $stmt = $this->conn->prepare($sql);
        $stmt->execute();
        return $stmt->fetchAll();
    }

    public function getById($id)
    {
        $sql = "SELECT * FROM Atencion_Medica WHERE atm_id = :id";
        $stmt = $this->conn->prepare($sql);
        $stmt->bindParam(':id', $id);
        $stmt->execute();
        return $stmt->fetch();
    }

    public function create($motivo, $detalles, $ani_id, $doc_id, $fecha)
    {
        $sql = "INSERT INTO Atencion_Medica (atm_motivo, atm_detalles, ani_id, doc_id, atm_fecha_atencion, atm_estado)
                VALUES (:motivo, :detalles, :ani_id, :doc_id, :fecha, TRUE)";
        $stmt = $this->conn->prepare($sql);
        $stmt->bindParam(':motivo', $motivo);
        $stmt->bindParam(':detalles', $detalles);
        $stmt->bindParam(':ani_id', $ani_id);
        $stmt->bindParam(':doc_id', $doc_id);
        $stmt->bindParam(':fecha', $fecha);
        return $stmt->execute();
    }

    public function delete($id)
    {
        $sql = "UPDATE Atencion_Medica SET atm_estado = FALSE WHERE atm_id = :id";
        $stmt = $this->conn->prepare($sql);
        $stmt->bindParam(':id', $id);
        return $stmt->execute();
    }
}
