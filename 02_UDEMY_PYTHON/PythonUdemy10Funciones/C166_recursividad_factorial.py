print('***FACTORIAL DEL NUMERO***')

#Definir la función factorial recursiva
def factorial_recursiva(numero):
    #Caso Base
    if numero==0 or numero == 1:
        print(f' Factorial de {numero} es: 1') #1
        return 1
    else: # Caso recursivo
        factorial = numero * factorial_recursiva(numero - 1)
        print(f'Factorial de {numero} es: {factorial}')
        return factorial

#Programa Principal

numero = 0
numero = int(input('Ingrese el número para calcular su factorial:  '))
factorial = factorial_recursiva(numero)
print(f'Factorial Final de {numero} es {factorial} ')