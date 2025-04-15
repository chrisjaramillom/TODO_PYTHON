<?php
require_once "../app/helper/auth_helper.php";
if (session_status() === PHP_SESSION_NONE) {
    session_start();
}

class DiagnosticoController
{
    private $model;

    public function __construct()
    {
        require_once "../app/models/Diagnostico.php";
        $this->model = new Diagnostico();
    }

    public function index()
    {
        verificarPermisos('Diagnóstico', ['Administrador', 'Médico', 'Cuidador']);
        $diagnosticos = $this->model->getAll();
        require "../app/views/diagnostico/index.php";
    }

    public function show($id)
    {
        verificarPermisos('Diagnóstico', ['Administrador', 'Médico', 'Cuidador']);
        $diagnostico = $this->model->getById($id);
        require "../app/views/diagnostico/show.php";
    }

    public function create()
    {
        verificarPermisos('Diagnóstico', ['Administrador', 'Médico']);
        require "../app/views/diagnostico/create.php";
    }

    public function store()
    {
        verificarPermisos('Diagnóstico', ['Administrador', 'Médico']);

        if ($_SERVER['REQUEST_METHOD'] === 'POST') {
            $enfermedad = $_POST['enfermedad'];
            $sintomas = $_POST['sintomas'];
            $tratamiento = $_POST['tratamiento'];
            $medicamentos = $_POST['medicamentos'];
            $atm_id = $_POST['atm_id'];

            $this->model->create($enfermedad, $sintomas, $tratamiento, $medicamentos, $atm_id);
            header("Location: /refugio_mvc/public/diagnostico/index");
            exit();
        }
    }

    public function delete($id)
    {
        verificarPermisos('Diagnóstico', ['Administrador', 'Médico']);
        $this->model->delete($id);
        header("Location: /refugio_mvc/public/diagnostico/index");
        exit();
    }
}
