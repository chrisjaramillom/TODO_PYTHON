# Manipulación de Archivos en Python
# -*- coding: utf-8 -*-
import os

nombre_archivo = 'archivo.txt'

# Verifica si el archivo existe para decidir el modo de apertura
modo = 'a' if os.path.isfile(nombre_archivo) else 'w'

# Abre el archivo en el modo adecuado (con with para cierre automático)
with open(nombre_archivo, modo, encoding='utf-8') as archivo:
    archivo.write('Este texto se agregará sin borrar lo anterior.\n')
    archivo.write('¡Manejo seguro de archivos con Python!\n')