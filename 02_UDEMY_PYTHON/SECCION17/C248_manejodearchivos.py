try:
    archivo = open('archivo.txt', 'w', encoding='utf-8')
    archivo.write('Hola, soy un archivo de texto.\n')
    archivo.write('Este es un archivo de texto.\n')
    archivo.close()

    archivo = open('archivo.txt', 'a', encoding='utf-8')
    # Abre el archivo en modo 'a' para agregar contenido sin borrar lo anterior con tildes y caracteres especiales
    archivo.write('SEGUNDA CORRIDA!!!.\n')
    archivo.write('Este ó es un archivo de texto.\n')
    archivo.close()
except Exception as e:  
    print(f"Ocurrió un error ó al manejar el archivo: {e}")
finally:
    # Asegúrate de cerrar el archivo si está abierto
    try:
        archivo.close()
    except NameError:
        pass
# El bloque finally asegura que el archivo se cierre, incluso si ocurre un error.
    