print('***INGRESO AL SISTEMA***')

USUARIO = 'Admin'
CONTRASENIA = '123'

user = input('Ingrese USUARIO: ').strip()
passw = input('Ingrese CONTRASEÑA: ').strip()

if USUARIO == user and CONTRASENIA == passw:
    print('\nBIENVENIDO AL SISTEMA 1!!!')
elif not USUARIO == user and CONTRASENIA == passw:
    print('\nUSUARIO equivocado 1')
elif USUARIO == user and not CONTRASENIA == passw:
    print('\nCONSTRASEÑA equivocada 1')
elif not USUARIO == user and not CONTRASENIA == passw:
    print('\nUSUARIO y CONSTRASEÑA equivocados 1')
else:
    print('\nERROR EN EL SISTEMA VUEVA A INTENTARLO 1')


if USUARIO == user and CONTRASENIA == passw:
    print('BIENVENIDO AL SISTEMA 2!!!')
elif CONTRASENIA == passw:
    print('USUARIO equivocado 2')
elif USUARIO == user:
    print('CONSTRASEÑA equivocada 2')
else:
    print('USUARIO y CONSTRASEÑA equivocados 2')