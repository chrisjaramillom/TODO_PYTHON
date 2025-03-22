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
}
