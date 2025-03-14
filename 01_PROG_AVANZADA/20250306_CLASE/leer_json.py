import json

# Datos que vamos a guardar en un archivo JSON
estudiantes = [
    {"nombre": "Juan", "edad": 20, "carrera": "Ingeniería en Computación"},
    {"nombre": "María", "edad": 21, "carrera": "Ingeniería en Computación"},
    {"nombre": "Pedro", "edad": 22, "carrera": "Ingeniería en Computación"}
]

# Guardar los datos en un archivo JSON
with open("estudiantes.json", "w") as archivo:
    json.dump(estudiantes, archivo, indent=4)
    print("Datos guardados en el archivo estudiantes.json")
    
# Leer los datos de un archivo JSON
with open("estudiantes.json", "r") as archivo:
    datos = json.load(archivo)
    print("Datos leídos del archivo estudiantes.json")
    print(datos)

# Mostrar los datos leídos
for estudiante in datos:
    print(f"Nombre: {estudiante['nombre']}")
    print(f"Edad: {estudiante['edad']}")
    print(f"Carrera: {estudiante['carrera']}")
    print()

