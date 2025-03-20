<?php
require_once "../app/config/database.php";

class Animal
{
    private $conn;

    public function __construct()
    {
        $db = new Database();
        $this->conn = $db->connect();
    }

    // Obtener todos los animales
    public function getAll()
    {
        $query = "SELECT * FROM Animal WHERE ani_estado = TRUE";
        $stmt = $this->conn->prepare($query);
        $stmt->execute();
        return $stmt->fetchAll();
    }

    // Obtener un animal por ID
    public function getById($id)
    {
        $query = "SELECT * FROM Animal WHERE ani_id = :id AND ani_estado = TRUE";
        $stmt = $this->conn->prepare($query);
        $stmt->bindParam(':id', $id, PDO::PARAM_INT);
        $stmt->execute();
        return $stmt->fetch();
    }

    // Agregar un nuevo animal
    public function create($nombre, $especie, $tipo, $raza, $fecha_ingreso, $lugar_recogida, $sexo, $cui_id)
    {
        $query = "INSERT INTO Animal (ani_nombre, ani_especie, ani_tipo, ani_raza, ani_fecha_ingreso, ani_lugar_recogida, ani_sexo, cui_id, ani_estado) 
                  VALUES (:nombre, :especie, :tipo, :raza, :fecha_ingreso, :lugar_recogida, :sexo, :cui_id, TRUE)";
        $stmt = $this->conn->prepare($query);
        $stmt->bindParam(':nombre', $nombre);
        $stmt->bindParam(':especie', $especie);
        $stmt->bindParam(':tipo', $tipo);
        $stmt->bindParam(':raza', $raza);
        $stmt->bindParam(':fecha_ingreso', $fecha_ingreso);
        $stmt->bindParam(':lugar_recogida', $lugar_recogida);
        $stmt->bindParam(':sexo', $sexo);
        $stmt->bindParam(':cui_id', $cui_id, PDO::PARAM_INT);
        return $stmt->execute();
    }

    // Actualizar datos de un animal
    public function update($id, $nombre, $especie, $tipo, $raza, $fecha_ingreso, $lugar_recogida, $sexo, $cui_id)
    {
        $query = "UPDATE Animal SET ani_nombre = :nombre, ani_especie = :especie, ani_tipo = :tipo, ani_raza = :raza, 
                  ani_fecha_ingreso = :fecha_ingreso, ani_lugar_recogida = :lugar_recogida, ani_sexo = :sexo, cui_id = :cui_id 
                  WHERE ani_id = :id";
        $stmt = $this->conn->prepare($query);
        $stmt->bindParam(':nombre', $nombre);
        $stmt->bindParam(':especie', $especie);
        $stmt->bindParam(':tipo', $tipo);
        $stmt->bindParam(':raza', $raza);
        $stmt->bindParam(':fecha_ingreso', $fecha_ingreso);
        $stmt->bindParam(':lugar_recogida', $lugar_recogida);
        $stmt->bindParam(':sexo', $sexo);
        $stmt->bindParam(':cui_id', $cui_id, PDO::PARAM_INT);
        $stmt->bindParam(':id', $id, PDO::PARAM_INT);
        return $stmt->execute();
    }

    // Eliminación lógica de un animal
    public function delete($id)
    {
        $query = "UPDATE Animal SET ani_estado = FALSE WHERE ani_id = :id";
        $stmt = $this->conn->prepare($query);
        $stmt->bindParam(':id', $id, PDO::PARAM_INT);
        return $stmt->execute();
    }
}
