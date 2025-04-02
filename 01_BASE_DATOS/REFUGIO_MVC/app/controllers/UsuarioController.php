<?php
require_once "../app/models/Usuario.php";
require_once "../app/helper/auth_helper.php";


session_start();
verificarRol(['Administrador']); // Solo admin accede

class UsuarioController
{
    private $model;

    public function __construct()
    {
        $this->model = new Usuario();
    }

    public function index()
    {
        $usuarios = $this->model->getAll();
        require "../app/views/usuario/index.php";
    }

    public function create()
    {
        require "../app/views/usuario/create.php";
    }

    public function store()
    {
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            $nombre = $_POST['nombre'];
            $email = $_POST['email'];
            $password = password_hash($_POST['password'], PASSWORD_DEFAULT);
            $rol = $_POST['rol'];

            // Validar que el email no exista
            if ($this->model->existeEmail($email)) {
                $_SESSION['error'] = "El correo ya está registrado.";
                header("Location: /refugio_mvc/public/usuario/create");
                exit();
            }

            // Si es nuevo, crear el usuario
            $this->model->crear($nombre, $email, $password, $rol);
            header("Location: /refugio_mvc/public/usuario/index");
            exit();
        }
    }


    public function delete($id)
    {
        $this->model->desactivar($id);
        header("Location: /refugio_mvc/public/usuario/index");
        exit();
    }
}
