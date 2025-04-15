<?php
require_once "../app/helper/auth_helper.php";
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}
verificarPermisos('Animales', ['Administrador', 'Cuidador', 'Médico']);

class AnimalController
{
    private $model;

    public function __construct()
    {
        require_once "../app/models/Animal.php";
        $this->model = new Animal();
    }

    public function index()
    {
        $animales = $this->model->getAll();
        require "../app/views/animal/index.php";
    }

    public function show($id)
    {
        $animal = $this->model->getById($id);
        require "../app/views/animal/show.php";
    }

    public function create()
    {
        require "../app/views/animal/create.php";
    }

    public function store()
    {
        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            $nombre = $_POST['nombre'];
            $especie = $_POST['especie'];
            $tipo = $_POST['tipo'];
            $raza = $_POST['raza'];
            $fecha = $_POST['fecha'];
            $lugar = $_POST['lugar'];
            $sexo = $_POST['sexo'];
            $cui_id = $_POST['cui_id'];

            $this->model->create($nombre, $especie, $tipo, $raza, $fecha, $lugar, $sexo, $cui_id);
            header("Location: /refugio_mvc/public/animal/index");
            exit();
        }
    }

    public function delete($id)
    {
        $this->model->delete($id);
        header("Location: /refugio_mvc/public/animal/index");
        exit();
    }
}
