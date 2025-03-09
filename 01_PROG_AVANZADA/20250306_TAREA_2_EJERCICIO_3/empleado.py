## Archivo: Empleado.py
class Empleado:
    def __init__(self, nombre, edad, salario,):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        self.trabajando = False

    def trabajar(self):
        self.trabajando = not self.trabajando
        if self.trabajando:
            return f"{self.nombre} ha comenzado a trabajar."
        else:
            return f"{self.nombre} ha dejado de trabajar."
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Salario: {self.salario}"
    