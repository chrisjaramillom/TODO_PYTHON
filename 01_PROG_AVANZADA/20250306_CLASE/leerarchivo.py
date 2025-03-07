
# Leer el archivo archivo.txt y mostrar su contenido en pantalla.
# Abre el archivo en modo lectura
# with open("archivo.txt", "r") as cualquiere_archivo:

try:
    with open("archivo.txt", "r") as cualquiere_archivo:  # C:\\Users\\CHRISTIAN\\PycharmProjects\\PROGRAMACION_AVANZADA\\20250306_CLASE el path debe ser con doble barra vertical
        # print(cualquiere_archivo.read())  # Muestra el contenido del archivo
        contenido = cualquiere_archivo.read()
        print(contenido)
        print(type(contenido))
except FileNotFoundError:
    print("El archivo no existe")
except PermissionError:
    print("No tiene permisos para abrir el archivo")
except Exception as e:
    print(f"Error: {e}")
finally:
    print("Fin del programa")
    