import math

print('*** Constantes en Python ***')

PI = 3.14159
print('El Valor de PI es:', PI)

NOMBRE_BASE_DATOS = 'clientes _bd'
print('Nombre de la base de datos es:' , NOMBRE_BASE_DATOS)

# Esto no se debe hacer, no se debe modificar el valor de una constante
# Las constantes en Python se definen en mayúsculas
# Por su condición dinámica Python deja asignar varios valores una constante, pero no se debe.

NOMBRE_BASE_DATOS = 'listado_clientes_db'
print('Cambia nombre de la base a pesar de ser constante:' , NOMBRE_BASE_DATOS)

# Usar una constante del lenguaje Python

print('Valor de PI en la librería math:', math.pi)
