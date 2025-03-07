print('***LISTAS Y DICCIONARIOS***')

personas = [
    {
        'nombre': 'carlos',
        'apellido': 'jara',
        'edad': 30,
    },
    {
        'nombre': 'maria',
        'apellido': 'flores',
        'edad': 21,
    }
]

for persona in personas:
    print(f'- {persona}')

#Acceder a un diccionario desde una lista

print(f'''
    Nombre:{personas[0].get('nombre')}
    Apellido:{personas[0].get('apellido')}
    Edad:{personas[0].get('edad')}
''')

# Recorrer los elementos de la lista
print('Impresion Método 1')
for contador, persona in enumerate(personas):
    print(f'{contador+1} - Persona: {persona}')

print('\nImpresion Método 2')
for contador, persona in enumerate(personas):
    print(f'Detalle: Nombre: {persona.get('nombre')}, Apellido: {persona.get('apellido')}, Edad: {persona.get('edad')}')
