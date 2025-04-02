<?php
require_once "../app/config/config.php";
require_once APPROOT . "/helper/auth_helper.php";
require_once "../app/models/Diagnostico.php";

session_start();
verificarRol(['Administrador', 'Doctor']);

class DiagnosticoController
{
    private $model;

    public function __construct()
    {
        $this->model = new Diagnostico();
    }

    public function index($atm_id)
    {
        $diagnosticos = $this->model->getByAtencion($atm_id);
        require "../app/views/diagnostico/index.php";
    }

    public function store($atm_id)
    {
        if ($_SERVER["REQUEST_METHOD"] === "POST") {
            $enfermedad = $_POST["enfermedad"];
            $sintomas = $_POST["sintomas"];
            $tratamiento = $_POST["tratamiento"];
            $medicamentos = $_POST["medicamentos"];

            $this->model->create($atm_id, $enfermedad, $sintomas, $tratamiento, $medicamentos);
            header("Location: /refugio_mvc/public/diagnostico/index/$atm_id");
            exit();
        } else {
            require "../app/views/diagnostico/create.php";
        }
    }

    public function delete($id)
    {
        $this->model->delete($id);
        // Lo ideal sería redirigir a la atención correspondiente
        header("Location: /refugio_mvc/public/atencionmedica/index");
        exit();
    }
}
