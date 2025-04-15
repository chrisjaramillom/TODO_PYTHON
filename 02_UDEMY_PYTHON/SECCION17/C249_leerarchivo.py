#Lectura de archivos en Python
# -*- coding: utf-8 -*-

# Abre el archivo en modo lectura (r) con codificación UTF-8
archivos = open('archivo2.txt', 'r', encoding='utf-8')
# Lee el contenido del archivo

# Desabilitado para el siguiente ejemplo
# leer todo el archivo
#print(archivos.read())
#archivos.close()

#Desabilitado para el siguiente ejemplo
# leer algunos caracteres
#print(archivos.read(3)) # Lee los primeros 5 caracteres
#print(archivos.read(7)) # Lee los siguientes 5 caracteres

#Desabilitado para el siguiente ejemplo
# Leer líneas completas
#print(archivos.readline()) # Lee la primera línea
#print(archivos.readline()) # Lee la segunda línea

#Iterar sobre el archivo
#for linea in archivos:
#    print(linea.strip())  # Imprime cada línea sin saltos de línea adicionales
# Cerrar el archivo
#archivos.close()

# Leer todas las líneas y almacenarlas en una lista
#print(archivos.readlines())

# Leer todas las líneas y almacenarlas en una lista
#lineas = archivos.readlines()
# Imprimir la lista de líneas
#for linea in lineas:
#    print(linea.strip())  # Imprime cada línea sin saltos de línea adicionales
# Cerrar el archivo
#archivos.close()

#Leer todas las líneas y almacenarlas en una lista
#print(archivos.readlines()[7])

#Copia de archivos
# -*- coding: utf-8 -*-
archivodos = open('copia.txt', 'a', encoding='utf-8')
archivodos.write(archivos.read())

archivos.close()
archivodos.close()
print("Archivo copiado con éxito.")











