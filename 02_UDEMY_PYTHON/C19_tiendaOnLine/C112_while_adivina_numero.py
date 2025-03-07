# Realizar un sistema para adivinar un número del 0 al 50
# el sistema debe validar que el número sea asigando randomincamente

print('***ADIVINA ADIVINADOR***')

import random
contador = 0
INTENTOS = 10

aleatorio = random.randint(0, 50)

print('Debes adivinar el número del 0 al 50')
print(f'{aleatorio}')
adivinador = int(input('Ingrese el número: '))

while aleatorio != adivinador and INTENTOS < 10:
    print(f'En número es incorrecto')
    if aleatorio > adivinador:
        print('En número ingresado es mayor que el requerido')
    else:
        print('En número ingresado es menor que el requerido')
    contador += 1
    print(f'Te quedan {10 - contador} oportunidades')
    if contador == INTENTOS:
        print(f'El número secreto era: {aleatorio}')
        print('Has llegado al máximo de oportunidades.   ADIOS!!!!')
        break
    else:
        adivinador = int(input('Ingrese el número: '))
else:
    print(f'Tu adivinaste el número en {contador} oportunidades.  FELICITACIONES!!!')