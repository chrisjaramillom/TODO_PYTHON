<?php
require_once "../app/helper/auth_helper.php";
session_start();

class AtencionMedicaController
{
    private $conn;
    private $model;

    public function __construct()
    {
        require_once "../app/models/AtencionMedica.php";
        require_once "../app/models/Animal.php";
        require_once "../app/models/Doctor.php";
        $db = new Database();
        $this->conn = $db->connect();
        $this->model = new AtencionMedica();
    }

    public function index()
    {
        verificarPermisos('Atención Médica', ['Administrador', 'Médico', 'Cuidador']);
        $atenciones = $this->model->getAll();
        require "../app/views/atencion/index.php";
    }

    public function show($id)
    {
        verificarPermisos('Atención Médica', ['Administrador', 'Médico', 'Cuidador']);
        $atencion = $this->model->getById($id);
        require "../app/views/atencion/show.php";
    }

    public function create()
    {
        verificarPermisos('Atención Médica', ['Administrador', 'Médico']);
        $animalModel = new Animal();
        $doctorModel = new Doctor();
        $animales = $animalModel->getAll();
        $doctores = $doctorModel->getAll();
        require "../app/views/atencion/create.php";
    }

    public function store()
    {
        verificarPermisos('Atención Médica', ['Administrador', 'Médico']);

        if ($_SERVER["REQUEST_METHOD"] === "POST") {
            $motivo = $_POST["motivo"];
            $detalles = $_POST["detalles"];
            $ani_id = $_POST["ani_id"];
            $doc_id = $_POST["doc_id"];
            $fecha = $_POST["fecha_atencion"];

            $sqlAtencion = "INSERT INTO Atencion_Medica (atm_motivo, atm_detalles, ani_id, doc_id, atm_fecha_atencion, atm_estado)
                            VALUES (:motivo, :detalles, :ani_id, :doc_id, :fecha, TRUE)";
            $stmt = $this->conn->prepare($sqlAtencion);
            $stmt->bindParam(':motivo', $motivo);
            $stmt->bindParam(':detalles', $detalles);
            $stmt->bindParam(':ani_id', $ani_id);
            $stmt->bindParam(':doc_id', $doc_id);
            $stmt->bindParam(':fecha', $fecha);
            $stmt->execute();

            $atm_id = $this->conn->lastInsertId();

            if (!empty($_POST['diagnosticos'])) {
                $diagnosticos = $_POST['diagnosticos'];

                $sqlDiag = "INSERT INTO Diagnostico (diag_enfermedad, diag_sintomas, diag_tratamiento, diag_medicamentos, atm_id, diag_estado)
                            VALUES (:enfermedad, :sintomas, :tratamiento, :medicamentos, :atm_id, TRUE)";
                $stmtDiag = $this->conn->prepare($sqlDiag);

                foreach ($diagnosticos as $diag) {
                    $stmtDiag->bindParam(':enfermedad', $diag['enfermedad']);
                    $stmtDiag->bindParam(':sintomas', $diag['sintomas']);
                    $stmtDiag->bindParam(':tratamiento', $diag['tratamiento']);
                    $stmtDiag->bindParam(':medicamentos', $diag['medicamentos']);
                    $stmtDiag->bindParam(':atm_id', $atm_id);
                    $stmtDiag->execute();
                }
            }

            header("Location: /refugio_mvc/public/atencionmedica/index");
            exit();
        } else {
            $this->create();
        }
    }

    public function delete($id)
    {
        verificarPermisos('Atención Médica', ['Administrador', 'Médico']);
        $this->model->delete($id);
        header("Location: /refugio_mvc/public/atencionmedica/index");
        exit();
    }
}
