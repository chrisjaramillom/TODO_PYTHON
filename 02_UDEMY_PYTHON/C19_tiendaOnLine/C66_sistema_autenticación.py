print('***SISTEMA DE AUTENTICACIÓN***')
print('No se diferencian mayúsculas de minúsculas')

USUARIO = 'admin'
CONTRASENIA = '123'

usuario = input('Ingrese su usuario: ')
contrasenia = input('Ingrese su contraseña: ')

autenticacion = (usuario.strip().lower() == USUARIO
                         and contrasenia.strip().lower() == CONTRASENIA)
print(f'\nSu autenticación ha salido: {autenticacion} ')

print('\n***SISTEMA DE AUTENTICACIÓN***')
print('Con diferenciación de mayúsculas y minúsculas')
autenticacion = (usuario.strip() == USUARIO
                         and contrasenia.strip() == CONTRASENIA)
print(f'\nSu autenticación ha salido: {autenticacion} ')