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
                // Guardar solo los datos necesarios en la sesión
                $_SESSION['usuario'] = [
                    'id' => $datos['usr_id'],
                    'nombre' => $datos['usr_nombre'],
                    'rol' => $datos['usr_rol'],
                    'email' => $datos['usr_email']
                ];

                header("Location: /refugio_mvc/public/animal/index");
                exit();
            } else {
                $_SESSION['error'] = "Credenciales incorrectas";
                header("Location: /refugio_mvc/public/auth/login");
                exit();
            }
        }
    }

    public function logout()
    {
        session_destroy();
        header("Location: /refugio_mvc/public/auth/login");
    }
}
