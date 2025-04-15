<?php
require_once "../app/helper/auth_helper.php";
require_once "../app/models/Usuario.php";

if (session_status() === PHP_SESSION_NONE) {
    session_start();
}

class UsuarioController
{
    private $model;

    public function __construct()
    {
        $this->model = new Usuario();
    }

    public function index()
    {
        verificarPermisos('Usuarios', ['Administrador']);
        $usuarios = $this->model->getAll();
        require "../app/views/usuario/index.php";
    }

    public function create()
    {
        verificarPermisos('Usuarios', ['Administrador']);
        require "../app/views/usuario/create.php";
    }

    public function store()
    {
        verificarPermisos('Usuarios', ['Administrador']);

        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            $nombre = $_POST['nombre'];
            $email = $_POST['email'];
            $password = password_hash($_POST['password'], PASSWORD_DEFAULT);
            $rol = $_POST['rol'];

            // Validar si ya existe el correo
            if ($this->model->existeEmail($email)) {
                $_SESSION['error'] = "El correo ya está registrado.";
                header("Location: /refugio_mvc/public/usuario/create");
                exit();
            }

            // Crear nuevo usuario
            $this->model->crear($nombre, $email, $password, $rol);
            header("Location: /refugio_mvc/public/usuario/index");
            exit();
        }
    }

    public function delete($id)
    {
        verificarPermisos('Usuarios', ['Administrador']);
        $this->model->delete($id);
        header("Location: /refugio_mvc/public/usuario/index");
        exit();
    }
}
