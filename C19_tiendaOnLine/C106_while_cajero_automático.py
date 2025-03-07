# Realizar un sistema que simule un cajero automático
# debe tener saldo inicial, aumentar si hay depósito y restar si existe un retiro.

print('***CAJERO AUTOMÁTICO***')

salir = False
saldo = 2000
while not salir:
    print(f''' **Menú Principal**
    1. Consultar Saldo
    2. Realizar Deposito
    3. Realizar Retiro
    4. SALIR
    ''')
    opcion = int(input('Seleccione una opción: '))
    if opcion == 1:
        print(f'Tu saldo es: $ {saldo:.2f} USD\n')
    elif opcion == 2:
        deposito = float(input('Ingresar cantidad del deposito\n'))
        saldo += deposito
        print(f'Tu saldo es: $ {saldo:.2f} USD\n')
    elif opcion == 3:
        retiro = float(input('Confirmar cantidad del retiro\n'))
        if retiro>saldo:
            print(f'Tu saldo es menor que el monto requerido.  Saldo Actual: $ {saldo:.2f} USD\n')
        else:
            saldo -= retiro
            print(f'Tu saldo es: $ {saldo:.2f} USD\n')
    elif opcion == 4:
        print('Gracias ADIOS\n')
        salir = True
    else :
        print('Opción INVALIDA\n')
else:
    print('SISTEMA FUERA DE LINEA')