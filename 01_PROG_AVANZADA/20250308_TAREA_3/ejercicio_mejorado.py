class RegistroProductos:
    def __init__(self, archivo_csv):
        self.archivo_csv = archivo_csv
        self.crear_archivo()

    def crear_archivo(self):
        """Crea el archivo CSV si no existe, asegurando que los encabezados estén presentes."""
        try:
            with open(self.archivo_csv, 'r', encoding='utf-8') as archivo:
                contenido = archivo.readlines()
                if not contenido:  # Si el archivo está vacío, escribir los encabezados
                    with open(self.archivo_csv, 'w', encoding='utf-8') as nuevo_archivo:
                        nuevo_archivo.write("Nombre del producto,Categoría,Precio\n")
        except FileNotFoundError:
            with open(self.archivo_csv, 'w', encoding='utf-8') as archivo:
                archivo.write("Nombre del producto,Categoría,Precio\n")

    def agregar_producto(self, nombre, categoria, precio):
        """Agrega un producto al archivo CSV si el precio es válido."""
        try:
            precio = float(precio)  # Validar que el precio sea un número
            with open(self.archivo_csv, 'a', encoding='utf-8') as archivo:
                archivo.write(f"{nombre},{categoria},{precio}\n")
                print("Producto agregado correctamente.")
        except ValueError:
            print("Error: El precio debe ser un número válido.")

    def mostrar_contenido(self):
        """Muestra el contenido del archivo CSV."""
        try:
            with open(self.archivo_csv, 'r', encoding='utf-8') as archivo:
                for linea in archivo:
                    print(linea.strip())  # strip() elimina los saltos de línea
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
