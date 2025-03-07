# Realizar un sistema que simule un password
# el sistema debe validar que el password tenga 6 o más caracteres

print('***PASSWORD***')

clave = input('Ingrese su contraseña: ')

while len(clave) < 6:
    print(f'Su contraseña no es valida, al menos 6 caracteres')
    clave = input('Ingrese su contraseña: ')
else:
    print('Su contraseña ha sido ACEPTADA, Adios!!!')