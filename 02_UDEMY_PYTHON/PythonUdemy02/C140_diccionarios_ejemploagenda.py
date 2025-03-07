print('***AGENDA DE CONTACTOS***')

# Ejemplo para crear una agenda de telefonos

# Creamos un diccionario de personas con clave y valor

agenda = {
    'Carlos': {
        'telefono': '123456',
        'mail': 'carlos@correo.com',
        'direccion': 'Sanqolqui',
    },
    'Maria': {
        'telefono': '234567',
        'mail': 'maria@correo.com',
        'direccion': 'Quito',
    },
    'Pedro': {
        'telefono': '345678',
        'mail': 'pedro@correo.com',
        'direccion': 'Atacames',
    }
}

print(f'Diccionario de persona: {agenda}')

#Acceder a la información de un contacto en específico
print(f'''Información del contacto de María:
    Teléfono: {agenda['Maria']['telefono']}
    Email: {agenda['Maria']['mail']}
    Dirección: {agenda['Maria']['direccion']}
''')

# Agregar un nuevo contacto
agenda['Ana'] = {
    'telefono': '456789',
    'mail': 'ana@correo.com',
    'direccion': 'Ambato'
}

print(f'Diccionario de persona: {agenda}')

# Eliminar contacto existente
agenda.pop('Pedro')
del agenda['Ana']

#Mostrar los contactos de la agenda
print('\n Contactos en la Agenda')
for nombre, detalles in agenda.items():
    print(f'''Nombre: {nombre}
    Telefono: {detalles.get('telefono')}
    Email: {detalles.get('mail')}
    Dirección: {detalles.get('direccion')}
''')
