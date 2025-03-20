<?php
require_once "../app/models/Animal.php";

class AnimalController
{
    private $model;

    public function __construct()
    {
        $this->model = new Animal();
    }

    // Método para mostrar todos los animales
    public function index()
    {
        $animales = $this->model->getAll();
        require "../app/views/animal/index.php"; // Carga la vista con los datos
    }

    // Método para mostrar un animal por ID
    public function show($id)
    {
        $animal = $this->model->getById($id);
        require "../app/views/animal/show.php"; // Carga la vista con los detalles del animal
    }

    // Método para agregar un nuevo animal
    public function store()
    {
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            $nombre = $_POST["nombre"];
            $especie = $_POST["especie"];
            $tipo = $_POST["tipo"];
            $raza = $_POST["raza"];
            $fecha_ingreso = $_POST["fecha_ingreso"];
            $lugar_recogida = $_POST["lugar_recogida"];
            $sexo = $_POST["sexo"];
            $cui_id = $_POST["cui_id"];

            $this->model->create($nombre, $especie, $tipo, $raza, $fecha_ingreso, $lugar_recogida, $sexo, $cui_id);
            header("Location: /refugio_mvc/public/animal/index");
            exit();
        } else {
            require "../app/views/animal/create.php"; // Carga el formulario de creación
        }
    }

    // Método para eliminar un animal (eliminación lógica)
    public function delete($id)
    {
        $this->model->delete($id);
        header("Location: /refugio_mvc/public/animal/index");
        exit();
    }
}
