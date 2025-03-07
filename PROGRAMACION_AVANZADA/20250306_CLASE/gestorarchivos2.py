# TAREA 

class GestorArchivos2:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo

    def crear_archivo(self):
        try:
            with open(self.nombre_archivo, 'w') as archivo:
                archivo.write("Nombre,Apellido,Edad\n")
                print(f'Archivo {self.nombre_archivo} creado correctamente')
        except Exception as e:
            print(f'Error al crear el archivo: {e}')
    
    def leer_archivo(self):
        try:
            with open(self.nombre_archivo, 'r') as archivo:
                return archivo.read()
        except FileNotFoundError:
            print(f'El archivo {self.nombre_archivo} no existe')
            return None

    def escribir_archivo(self, contenido):
        try:
           with open(self.nombre_archivo, 'a') as archivo:
               archivo.write(contenido + '\n')
               print("Informacion agregada correctamente")
        except Exception as e:
            print(f'Error al escribir en el archivo: {e}')


#Programa Principal
# Crear la instancia de la clase
gestor = GestorArchivos2('datos.csv')

# Loop para agregar datos al archivo
while True:
    nombre = input("Ingrese el nombre (o escriba 'salir' para terminar): ")
    if nombre.lower() == 'salir':
        break

    apellido = input("Ingrese el apellido: ")
    edad = input("Ingrese la edad: ")

    # Escribir los datos en el archivo
    gestor.escribir_archivo(f"{nombre},{apellido},{edad}")

    # Mostrar el contenido actualizado
    print("\nContenido del archivo:")
    print(gestor.leer_archivo())


print("Fin del programa")
