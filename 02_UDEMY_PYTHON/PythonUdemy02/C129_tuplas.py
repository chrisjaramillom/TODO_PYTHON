# TUPLAS

print('***MANEJO DE TUPLAS***')

mi_tupla = (1, 2, 3, 4, 8)
print(mi_tupla)

# Los elementos de una tupla NO es actualizable
# mi_tupla.append(5) No ES POSIBLE

for elemento in mi_tupla:
    print(elemento, end=' ')

#Crear una tupla para una coordenada y, x
coordenadas = (3, 5)
# Accedemos a cada elemento de la tupla
print(f'\nCoordinada eje X: {coordenadas[0]}')
print(f'\nCoordinada eje Y: {coordenadas[1]}')

# Crear una tupla unitaria
tupla_un_elemento = 10,
print(tupla_un_elemento)

#Tuplas anidadas o tupla de tuplas
tuplas_anidadas = (1, (2, 3), (4, 'OTRO'))
print(tuplas_anidadas)
print(tuplas_anidadas[2])
print(tuplas_anidadas[2][1])

