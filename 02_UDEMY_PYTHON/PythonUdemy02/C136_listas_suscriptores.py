print('*** Lista de Suscriptores ***')

#Definimos el Set Inicial
#suscriptores = {} # Definimos un diccionario vacío, no se define un SET

suscriptores = set() # Define set vacío

# Agregar Suscriptores


print('***SISTEMA DE ADMINISTRACIÓN DE CUENTAS***')

salir = False

while not salir:
    print(f''' **Menú Principal SUSCRIPTORES**
    1. Agregar Suscriptor
    2. Eliminar Suscriptor
    3. Imprimir lista de Suscriptores
    4. SALIR
    ''')
    opcion = int(input('Seleccione una opción: '))
    if opcion == 1:
        suscriptores.add(input('Ingrese correo:\n').strip().lower())
    elif opcion == 2:
        eliminar = input('\nIngresar correo a eliminar:').strip().lower()
        if eliminar in suscriptores:
            suscriptores.remove(eliminar)
        else:
            print(f'El correo {eliminar} no es suscriptor')
    elif opcion == 3:
        print(f'**LISTA DE SUSCRIPTORES**\n')
        for suscriptor in suscriptores:
            print(f'- {suscriptor}')
    elif opcion == 4:
        print('Gracias ADIOS\n')
        salir = True
    else :
        print('Opción INVALIDA\n')