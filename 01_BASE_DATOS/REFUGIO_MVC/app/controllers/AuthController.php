<?php
require_once "../app/models/Usuario.php";
session_start();

class AuthController
{
    public function login()
    {
        require "../app/views/auth/login.php";
    }

    public function acceder()
    {
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            $email = $_POST['email'];
            $password = $_POST['password'];

            $usuario = new Usuario();
            $datos = $usuario->verificarLogin($email, $password);

            if ($datos) {
                $_SESSION['usuario'] = $datos;
                header("Location: /refugio_mvc/public/animal/index");
            } else {
                $_SESSION['error'] = "Credenciales incorrectas";
                header("Location: /refugio_mvc/public/auth/login");
            }
        }
    }

    public function logout()
    {
        session_destroy();
        header("Location: /refugio_mvc/public/auth/login");
    }
}
