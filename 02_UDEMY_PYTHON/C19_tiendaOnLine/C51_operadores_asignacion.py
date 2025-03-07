# OPERADORES DE ASIGNACIÓN

print('OPERADORES DE ASIGNACIÓN')
numero = 5
print(f'Valor asignado es: {numero}')

numero = 10
print(f'Valor asignado es: {numero}')

cadena = 'Hola 2025 allá voy'
print(f'Valor cadena asignada es: {cadena}')

#Asignación multiple

x, y, z = 10, 'Soy yo', -9.15
print(f'Valores x = {x}, y = {y}, z = {z}')

# Asignación multiple o intercambio de valores
# de una variable sin utilizar variables temporales

x, y = 10, 5
print(f'Valores Iniciales x = {x}, y = {y}')
x, y = y, x
print(f'Valores Intercambiados x = {x}, y = {y}')

# Recibir multiples valores de la entrada del usuario

nombre, apellido = input('Ingresa tu nombres y apellidos, separados por "," ').split(',')
print(f'Nombres: {nombre.strip()}, Apellido: {apellido.strip()}')

# Asignación encadenada, mismo valor a muchas variables

con1 = con2 = 'Soy yo'
print(f'Valores Cont1 = {con1}, cont2 = {con2}')

