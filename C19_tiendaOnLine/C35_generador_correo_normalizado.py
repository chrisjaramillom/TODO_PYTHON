# Generar un correo en base al nombre, la empresa y el dominio que se ingresa

nombre = 'Christian Alejandro Jaramillo Montufar'
nombre = nombre.strip()
normalizado = nombre.lower()
normalizado = normalizado.replace(' ', '.')

print('***Generador de Correos***')
print(f'Nombre del Colaborador: {nombre}')
print(f'Nombre Normalizado: {normalizado}')

empresa = 'GADMUR'
empresa = empresa.strip()
extension = '.gob.ec'

dominio = empresa.lower() + extension

print()
print('***Datos***')
print(f'Nombre de la Empresa: {empresa}')
print(f'Nombre Dominio: {dominio}')

print()
print('***Correo Electrónico***')
print(f'Correo del Colaborador: {normalizado}@{dominio}')


