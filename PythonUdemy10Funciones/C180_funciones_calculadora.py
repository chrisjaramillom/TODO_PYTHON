print('*** Sistema CALCULADORA ***')

def factores():
    factor1 = int(input('Ingresa primer factor:'))
    factor2 = int(input('Ingresa segundo factor:'))
    return(factor1, factor2)
def sumar():
    print('--- Suma de 2 factores ---')
    factor1, factor2 = factores()
    suma = factor1 + factor2
    print(f'{factor1} + {factor2} = {suma}')

def restar():
    print('--- Resta de 2 factores ---')
    factor1, factor2 = factores()
    resta = factor1 - factor2
    print(f'{factor1} - {factor2} = {resta}')

def multiplicar():
    print('--- Multiplicación de 2 factores ---')
    factor1, factor2 = factores()
    multi = factor1 * factor2
    print(f'{factor1} * {factor2} = {multi}')

def dividir():
    print('--- División de 2 factores ---')
    factor1, factor2 = factores()
    divid = factor1 / factor2
    print(f'{factor1} / {factor2} = {divid}')


# Programa principal
if __name__ == '__main__':
    # Creamos el menu
    while True:
        print(f'''Menú:
        1. SUMAR
        2. RESTAR
        3. MULTIPLICAR
        4. DIVIDIR
        5. TODAS LAS OPERACIONES        
        6. Salir''')
        opcion = int(input('Escoge una opción: '))
        if opcion == 1:
            sumar()
        elif opcion == 2:
            restar()
        elif opcion == 3:
            multiplicar()
        elif opcion == 4:
            dividir()
        elif opcion == 5:
            sumar()
            restar()
            multiplicar()
            dividir()
        elif opcion == 6:
            print('Regresa pronto!')
            break
        else:
            print('Opción inválida, proporciona otra opción!')
