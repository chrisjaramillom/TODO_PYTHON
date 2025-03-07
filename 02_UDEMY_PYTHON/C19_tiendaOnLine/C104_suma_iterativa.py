# Realizar la suma de los primeros 5 números
# utilizando un ciclo while

print('SUMA ITERATIVA')
MAXIMO = 5
numero = 1
acumulador_suma = 0

while numero <= MAXIMO:
    print(f'suma acumunada: {acumulador_suma} + {numero}' )
    acumulador_suma += numero
    numero += 1
    print(f'suma parcial: {acumulador_suma}')

print(f'Suma Acumulada: {acumulador_suma}')