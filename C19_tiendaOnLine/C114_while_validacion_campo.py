# Validación de un campo obligatorio
# Se intenta validar un campo para que el usuario no pueda
# ingresar datos vacios a un formulario con el while

print('VALIDACIÓN CAMPO FORMULARIO CON WHILE')

nombre_usuario = input('Ingresa tu nombre de usuario')

while not nombre_usuario:
    print('El valor ingresado NO es valido!!!')
    nombre_usuario = input('Ingresa tu nombre de usuario: ').strip().upper()
else:
    print(f'Has ingresado un nombre de usuario VALIDO, GRACIAS {nombre_usuario}!!!')