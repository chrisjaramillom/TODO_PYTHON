<?php require_once "../app/views/partials/menu.php"; ?>

<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <title>Registrar Atención Médica</title>
    <!-- Bootstrap CSS -->
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
</head>

<body class="bg-light">

    <div class="container py-4">
        <h2 class="text-center mb-4">Registrar Atención Médica con Diagnósticos</h2>

        <form action="/refugio_mvc/public/atencionmedica/store" method="POST" class="card p-4 shadow">

            <h5>Datos de Atención Médica</h5>
            <div class="row mb-3">
                <div class="col-md-6">
                    <label>Motivo</label>
                    <input type="text" name="motivo" class="form-control" required>
                </div>
                <div class="col-md-6">
                    <label>Detalles</label>
                    <input type="text" name="detalles" class="form-control" required>
                </div>
            </div>

            <div class="row mb-3">
                <div class="col-md-6">
                    <label>Animal</label>
                    <select name="ani_id" class="form-select" required>
                        <option value="">-- Seleccione un animal --</option>
                        <?php foreach ($animales as $animal): ?>
                            <option value="<?= $animal['ani_id'] ?>"><?= $animal['ani_nombre'] ?> (ID <?= $animal['ani_id'] ?>)</option>
                        <?php endforeach; ?>
                    </select>
                </div>
                <div class="col-md-6">
                    <label>Doctor</label>
                    <select name="doc_id" class="form-select" required>
                        <option value="">-- Seleccione un doctor --</option>
                        <?php foreach ($doctores as $doctor): ?>
                            <option value="<?= $doctor['doc_id'] ?>"><?= $doctor['doc_nombre'] ?> (ID <?= $doctor['doc_id'] ?>)</option>
                        <?php endforeach; ?>
                    </select>
                </div>
            </div>

            <div class="mb-3">
                <label>Fecha de Atención</label>
                <input type="date" name="fecha_atencion" class="form-control" required>
            </div>

            <hr>

            <h5>Diagnósticos</h5>
            <div id="diagnosticos-container" class="mb-3"></div>
            <button type="button" onclick="agregarDiagnostico()" class="btn btn-outline-primary mb-3">+ Agregar Diagnóstico</button>

            <div class="text-center">
                <button type="submit" class="btn btn-success">Registrar Atención</button>
                <a href="/refugio_mvc/public/atencionmedica/index" class="btn btn-secondary ms-2">Volver</a>
            </div>
        </form>
    </div>

    <script>
        let contador = 0;

        function agregarDiagnostico() {
            const contenedor = document.getElementById("diagnosticos-container");

            const bloque = document.createElement("div");
            bloque.className = "diagnostico-block border rounded p-3 mb-3 bg-white";

            bloque.innerHTML = `
            <h6>Diagnóstico ${contador + 1}</h6>
            <div class="mb-2">
                <label>Enfermedad:</label>
                <input type="text" name="diagnosticos[${contador}][enfermedad]" class="form-control" required>
            </div>
            <div class="mb-2">
                <label>Síntomas:</label>
                <textarea name="diagnosticos[${contador}][sintomas]" rows="2" class="form-control" required></textarea>
            </div>
            <div class="mb-2">
                <label>Tratamiento:</label>
                <textarea name="diagnosticos[${contador}][tratamiento]" rows="2" class="form-control" required></textarea>
            </div>
            <div class="mb-2">
                <label>Medicamentos / Indicaciones:</label>
                <textarea name="diagnosticos[${contador}][medicamentos]" rows="2" class="form-control" required></textarea>
            </div>
            <button type="button" class="btn btn-danger btn-sm" onclick="this.parentElement.remove()">Eliminar diagnóstico</button>
        `;

            contenedor.appendChild(bloque);
            contador++;
        }
    </script>

</body>

</html>