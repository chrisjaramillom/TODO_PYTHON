import os
import csv

class RegistroProductos:
    def __init__(self, archivo_csv):
        self.archivo_csv = archivo_csv
        self.crear_archivo()

    def crear_archivo(self):
        """Crea el archivo CSV si no existe, asegurando que los encabezados estén presentes."""
        if not os.path.exists(self.archivo_csv):
            with open(self.archivo_csv, mode='w', newline='', encoding='utf-8') as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow(["Nombre del producto", "Categoría", "Precio"])
                print(f"Archivo {self.archivo_csv} creado correctamente.")

    def agregar_producto(self, nombre, categoria, precio):
        """Agrega un producto al archivo CSV si el precio es válido."""
        try:
            precio = float(precio)  # Validar que el precio sea un número
            with open(self.archivo_csv, mode='a', newline='', encoding='utf-8') as archivo:
                escritor = csv.writer(archivo)
                escritor.writerow([nombre, categoria, precio])
                print("Producto agregado correctamente.")
        except ValueError:
            print("Error: El precio debe ser un número válido.")

    def mostrar_contenido(self):
        """Muestra el contenido del archivo CSV."""
        try:
            with open(self.archivo_csv, mode='r', encoding='utf-8') as archivo:
                lector = csv.reader(archivo)
                for fila in lector:
                    print(fila)
        except FileNotFoundError:
            print(f"El archivo {self.archivo_csv} no existe.")

# Crear una instancia del gestor de productos
gestor = RegistroProductos("productos.csv")

# Loop para ingresar productos
while True:
    nombre = input("Ingrese el nombre del producto (o escriba 'salir' para terminar): ").strip()
    if nombre.lower() == 'salir':
        break

    categoria = input("Ingrese la categoría del producto: ").strip()
    precio = input("Ingrese el precio del producto: ").strip()

    gestor.agregar_producto(nombre, categoria, precio)

    print("\nContenido actualizado del archivo:")
    gestor.mostrar_contenido()
    print("**********************")

print("Fin del programa")
# ¿Qué hace este programa?
# Este programa permite agregar productos a un archivo CSV llamado productos.csv.
# El programa solicita al usuario ingresar el nombre, categoría y precio de un producto.
# Si el precio es un número válido, el producto se agrega al archivo CSV.
# El contenido del archivo se muestra después de agregar cada producto.
# El programa termina cuando el usuario ingresa 'salir' como nombre del producto.
# ¿Qué hace la clase RegistroProductos?
# La clase RegistroProductos se encarga de gestionar los productos en un archivo CSV.
# Al crear una instancia de esta clase, se crea el archivo CSV si no existe.
# La clase tiene un método agregar_producto para agregar productos al archivo.
# El método mostrar_contenido muestra el contenido actual del archivo CSV.
# ¿Qué hace el método crear_archivo?
# El método crear_archivo crea el archivo CSV si no existe.
# Asegura que los encabezados del archivo estén presentes.
# ¿Qué hace el método agregar_producto?
# El método agregar_producto agrega un producto al archivo CSV.
# Verifica que el precio ingresado sea un número válido.
# ¿Qué hace el método mostrar_contenido?
# El método mostrar_contenido muestra el contenido del archivo CSV.
# Lee el archivo y muestra cada fila en la consola.
# ¿Qué hace el bucle while en el programa principal?
# El bucle while solicita al usuario ingresar productos.
# Cada producto se agrega al archivo CSV utilizando el método agregar_producto.
# Muestra el contenido actualizado del archivo después de agregar cada producto.
# ¿Qué hace el programa cuando el usuario ingresa 'salir'?
# El programa finaliza y muestra "Fin del programa" en la consola.
# ¿Qué mejoras harías a este programa?
# Podrías agregar validaciones adicionales, como verificar que el precio sea mayor que cero.
# Podrías permitir al usuario editar o eliminar productos del archivo CSV.
# Podrías agregar opciones de búsqueda y filtrado de productos.
# Podrías mejorar la presentación del contenido del archivo en la consola.
# Podrías manejar excepciones específicas para errores de lectura y escritura de archivos.
# Podrías agregar funciones para calcular estadísticas sobre los productos.
# Podrías permitir al usuario ingresar múltiples productos en una sola entrada.
    