<?php
require_once(__DIR__ . '/../helper/auth_helper.php');
require_once(__DIR__ . '/../models/Estadisticas.php');

if (session_status() === PHP_SESSION_NONE) {
    session_start();
}

class EstadisticasController
{
    private $model;

    public function __construct()
    {
        $this->model = new Estadistica();
    }

    public function animalesMasAtendidos()
    {
        verificarPermisos('Animales Más Atendidos', ['Médico']);
        $data = $this->model->getAnimalesMasAtendidos();
        require "../app/views/estadisticas/animales_mas_atendidos.php";
    }
}
