## Archivo: Programador.py
from empleado import Empleado

class Programador(Empleado):
    def __init__(self, nombre, edad, salario, lenguaje, proyectos):
        super().__init__(nombre, edad, salario)
        self.lenguaje = lenguaje
        self.proyectos = proyectos

    def codificar(self):
        return f"{self.nombre} está codificando en {self.lenguaje}."

    def revisar_proyecto(self):
        return f"{self.nombre} está revisando los proyectos: {', '.join(self.proyectos)}."

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Salario: {self.salario}, Lenguaje: {self.lenguaje}, Proyectos: {', '.join(self.proyectos)}"