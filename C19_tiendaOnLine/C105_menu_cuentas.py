# Realizar un sistema que simule la creación y eliminación de usuarios
# utilizando un menú dentro de un while y se ejecuta hasta que escoja el usuario SALIR

print('***SISTEMA DE ADMINISTRACIÓN DE CUENTAS***')

salir = False

while not salir:
    print(f''' **Menú Principal**
    1. Crear Cuenta
    2. Eliminar Cuenta
    3. SALIR
    ''')
    opcion = int(input('Seleccione una opción: '))
    if opcion == 1:
        print('Tu cuenta está CREADA\n')
    elif opcion == 2:
        print('Tu cuenta está ELIMINADA\n')
    elif opcion == 3:
        print('Gracias ADIOS\n')
        salir = True
    else :
        print('Opción INVALIDA\n')