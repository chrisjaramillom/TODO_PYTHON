## Archivo: Gerente.py
from empleado import Empleado

class Gerente(Empleado):
    def __init__(self, nombre, edad, salario, departamento, bono):
        super().__init__(nombre, edad, salario)
        self.departamento = departamento
        self.bono = bono

    def gestionar_departamento(self, departamento):
        self.departamento = departamento
        return f"El Gerente {self.nombre} gestiona el departamento de {self.departamento}."

    def otorgar_bono(self):
        return f"El Gerente {self.nombre} ha otorgado un bono de {self.bono} dólares."
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Salario: {self.salario}, Departamento: {self.departamento}, Bono: {self.bono}"
    
