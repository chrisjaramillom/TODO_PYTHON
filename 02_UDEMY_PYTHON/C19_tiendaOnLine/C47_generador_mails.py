# Generar un correo en base al nombre, la empresa y el dominio que se ingresa

print('***Datos Requeridos***\n')
nombres = input('Ingrese sus nombres completos:').strip()
nombres_normalizado = nombres.lower().replace(' ', '.')

apellidos = input('Ingrese sus nombres completos:')
apellidos_normalizado = apellidos.strip().lower().replace(' ', '.')

empresa = input('Ingrese su empresa:')
empresa_normalizada = empresa.strip().lower().replace(' ', '')

dominio = input('Ingrese su dominio:').strip().lower().replace(' ','')

print('\n***Generador de Correos***')
print(f'Nombre del Colaborador: {nombres} {apellidos}')
print('\n***Datos del Correo***')
print(f'Nombre de la Empresa: {empresa}')
print(f'Nombre Dominio: {dominio}')

print(f'''
***Correo Electrónico***
    Correo del Colaborador es: 
        {nombres_normalizado}.{apellidos_normalizado}@{empresa_normalizada}.{dominio}
        FIN!!!
    
''')

