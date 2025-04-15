<?php
require_once "../app/config/database.php";

class Usuario
{
    private $conn;

    public function __construct()
    {
        $db = new Database();
        $this->conn = $db->connect();
    }

    public function verificarLogin($email, $password)
    {
        $query = "SELECT * FROM Usuario WHERE usr_email = :email AND usr_estado = TRUE";
        $stmt = $this->conn->prepare($query);
        $stmt->bindParam(':email', $email);
        $stmt->execute();
        $usuario = $stmt->fetch();

        if ($usuario && password_verify($password, $usuario['usr_password'])) {
            return $usuario;
        }
        return false;
    }

    public function crear($nombre, $email, $password, $rol)
    {
        $sql = "INSERT INTO Usuario (usr_nombre, usr_email, usr_password, usr_rol, usr_estado)
            VALUES (:nombre, :email, :password, :rol, 1)";

        $stmt = $this->conn->prepare($sql);
        $stmt->bindParam(':nombre', $nombre);
        $stmt->bindParam(':email', $email);
        $stmt->bindParam(':password', $password);
        $stmt->bindParam(':rol', $rol);

        return $stmt->execute();
    }


    public function getAll()
    {
        $stmt = $this->conn->query("SELECT * FROM Usuario");
        return $stmt->fetchAll(PDO::FETCH_ASSOC);
    }

    public function existeEmail($email)
    {
        $sql = "SELECT COUNT(*) FROM Usuario WHERE usr_email = :email";
        $stmt = $this->conn->prepare($sql);
        $stmt->bindParam(':email', $email);
        $stmt->execute();
        return $stmt->fetchColumn() > 0;
    }

    public function delete($id)
    {
        $sql = "UPDATE Usuario SET usr_estado = 0 WHERE usr_id = :id";
        $stmt = $this->conn->prepare($sql);
        $stmt->bindParam(':id', $id);
        return $stmt->execute();
    }
}
