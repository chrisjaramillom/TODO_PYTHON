#definir clase estudiante 
import json

class Estudiante():
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        self.guardar_en_json() # Guardamos el estudiante en el archivo JSON
    
    def to_dict(self):
        """Devuelve un diccionario con los datos del estudiante."""
        return {
            "nombre": self.nombre,
            "edad": self.edad,
            "carrera": self.carrera
        }
    
    def guardar_en_json(self, archivo="estudiantes1.json"):
        """Guarda el estudiante en un archivo JSON agregándole a la lista existente."""
        try:
            with open(archivo, "r") as file:
                estudiantes = json.load(file)  # Cargamos los datos existentes
        except (FileNotFoundError, json.JSONDecodeError):
            estudiantes = []  # Si no existe el archivo o no tiene datos, creamos una lista vacía
        
        estudiantes.append(self.to_dict())  # Agregamos el estudiante actual a la lista
        
        with open(archivo, "w") as file:
            json.dump(estudiantes, file, indent=4)  # Guardamos la lista en el archivo JSON
        print(f"Estudiante {self.nombre} guardado en {archivo} JSON")
        
    
# Agregar estudiantes de forma interactiva
while True:
    nombre = input("Ingrese el nombre del estudiante (o 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break

    edad = input("Ingrese la edad: ")
    carrera = input("Ingrese la carrera: ")

    Estudiante(nombre, edad, carrera)  # Creamos una instancia de la clase Estudiante

print("\nPrograma finalizado")

