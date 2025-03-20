<?php
require_once "../app/models/Animal.php";

$animalModel = new Animal();

// Obtener todos los animales
$animales = $animalModel->getAll();
echo "<h2>Lista de Animales</h2>";
foreach ($animales as $animal) {
    echo "ID: " . $animal['ani_id'] . " - Nombre: " . $animal['ani_nombre'] . "<br>";
}

// Obtener un animal por ID
$animal = $animalModel->getById(1);
if ($animal) {
    echo "<h2>Detalles del Animal con ID 1</h2>";
    echo "Nombre: " . $animal['ani_nombre'] . "<br>";
} else {
    echo "<h2>No se encontró el animal con ID 1</h2>";
}
