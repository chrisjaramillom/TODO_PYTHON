class GestorArchivos:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        
    def leer_archivo(self):
        try:
            with open(self.nombre_archivo, "r") as cualquiere_archivo:
                contenido = cualquiere_archivo.read()
                return contenido
        except FileNotFoundError:
            print("El archivo {self.nombre_archivo} no existe")
            return None

    def escribir_archivo(self, contenido):
        try:
            with open(self.nombre_archivo, "a") as cualquiere_archivo:
                cualquiere_archivo.write(contenido)
                print("Se ha escrito el contenido")
        except FileNotFoundError:
            print("El archivo {self.nombre_archivo} no existe")
        except PermissionError:
            print("No tiene permisos para abrir el archivo")
        except Exception as e:
            print(f"Error: {e}")
    
    def reemplazar_archivo(self, contenido):
        try:
            with open(self.nombre_archivo, "w") as cualquiere_archivo:
                cualquiere_archivo.write(contenido)
                print("Se ha reemplazado el contenido")
        except FileNotFoundError:
            print("El archivo {self.nombre_archivo} no existe")
        except PermissionError:
            print("No tiene permisos para abrir el archivo")
        except Exception as e:
            print(f"Error: {e}")
    
    def crear_archivo(self):
        try:
            with open(self.nombre_archivo, "x") as cualquiere_archivo:
                print("Se ha creado el archivo")
        except FileExistsError:
            print("El archivo ya existe")
        except PermissionError:
            print("No tiene permisos para abrir el archivo")
        except Exception as e:
            print(f"Error: {e}")

gestor = GestorArchivos("archivo.txt")
contenido = gestor.leer_archivo()
print(contenido) # Muestra el contenido del archivo
print("**********************")
gestor.escribir_archivo("\nNUEVO TEXTO, Christian Jaramillo Montufar, 49 añitos\n")
print("**********************")
print(gestor.leer_archivo()) # Muestra el contenido del archivo
print("**********************")
gestor.reemplazar_archivo("Hola Mundo")

    