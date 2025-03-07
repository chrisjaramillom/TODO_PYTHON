# Dibujar un triángulo simétrico con el ingreso de filas

print('***Dibujo de un Triángulo Simétrico***')

filas = int(input('Ingrese número de filas: '))

for i in range(1, filas + 1):
    espacio_blanco = ' ' * (filas - i)
    asteriscos = '*' * (2 * i - 1)
    print(f'{espacio_blanco}{asteriscos}')
