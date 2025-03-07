# GENERADOR DE ID AUTOMÁTICO

from random import randint

# Valores ingresados por el usuario

print('\n****SISTEMA DE GENERADOR DE ID ÚNICO****')
cliente_nombre = input('Ingrese su nombre: ')
cliente_apellido = input('Ingrese su apellido:')
cliente_anio_nacimiento = input('Ingrese el año de nacimiento (YYYY):')

cliente_nombre2= cliente_nombre.strip().upper()[0:2]
cliente_apellido2= cliente_apellido.strip().upper()[0:2]
cliente_anio_nacimiento2= cliente_anio_nacimiento.strip()[2:]

numero_aleatorio = str(randint(1000,9999))


cliente_id = cliente_nombre2 + cliente_apellido2 + cliente_anio_nacimiento2 + numero_aleatorio

print('\n****DATOS DE SU ID****')
print(f'Hola {cliente_nombre} {cliente_apellido} ')
print('\tTu nuevo número de identificación (ID) generado por el sistema es:')
print(f'\t{cliente_id}')
print(f'\tFELICIDADES!!!')

