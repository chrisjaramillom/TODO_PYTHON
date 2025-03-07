class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f''' Persona:
        Nombre: {self.nombre} 
        Edad: {self.edad} años
        Dir. mem. {super.__str__(self)}'''

#Código Principal
persona1 = Persona("Juan", 25)
print(persona1) # El método __str__ se llama automáticamente desde el print
# print(persona1.__str__())   Opcional el argumento __str__