#Ejemplo de comprensión de listas

numeros = [1, 2, 3, 4, 5, 6]
print('Lista de Números:')
print(numeros)
pares = [par for par in numeros if par % 2 == 0]
print('Números Pares:')
print(pares)
impares = [imp for imp in numeros if imp % 2 != 0] # if es un filtrado de valores y es opcional
print('Números Impares:')
print(impares)

#Ejemplo de comprensión de listas 2
cuadrados = [x**2 for x in numeros]
print('Cuadrado de los Números:')
print(cuadrados)

numeros = range(10+1) # Tipo RANGO
print('OTRO EJEMPLO')
print('Lista de Números:')
print(numeros)
pares = [par for par in numeros if par % 2 == 0]
print('Números Pares:')
print(pares)

# Lista salundando a cada nombre
print('Ejemplo con Nombres')
nombres = ['Ana', 'Juan', 'Carlos']
saludando = [f'Hola {nombre}' for nombre in nombres]
print(saludando)