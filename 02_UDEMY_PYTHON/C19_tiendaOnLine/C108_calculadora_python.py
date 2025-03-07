# Realizar un sistema que simule una calculadora
# debe contar con las 4 operaciones básicas y el usuario ingresa los dos operandos

print('***CALCULADORA***')

salir = False

while not salir:
    print(f''' **Menú Principal calculadora**
    1. Suma
    2. Resta
    3. Multiplicación
    4. División
    5. SALIR
    ''')
    opcion = int(input('Seleccione una opción: '))
    if 1 <= opcion <= 4:
        operando1 = float(input('Ingrese el primer valor: '))
        operando2 = float(input('Ingrese el segundo valor: '))

    if opcion == 1:
        print(f'{operando1:.2f} + {operando2:.2f} = {(operando1 + operando2):.2f} \n')
    elif opcion == 2:
        print(f'{operando1:.2f} - {operando2:.2f} = {(operando1 - operando2):.2f} \n')
    elif opcion == 3:
        print(f'{operando1:.2f} * {operando2:.2f} = {(operando1 * operando2):.2f} \n')
    elif opcion == 4:
        if operando2 == 0:
            print('La división para CERO no es posible')
        else:
            print(f'{operando1:.2f} / {operando2:.2f} = {(operando1 / operando2):.2f} \n')
    elif opcion == 5:
        print('Gracias ADIOS\n')
        salir = True
    else :
        print('Opción INVALIDA\n')
else:
    print('SISTEMA FUERA DE LINEA')