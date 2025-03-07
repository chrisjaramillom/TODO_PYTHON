print('***DICCIONARIOS EN PYTHON***')

# Creamos un diccionario de persona con clave y valor

persona = {
    'nombre': 'Sergio',
    'edad': 30,
    'ciudad': 'Ecuador',
}

print(f'Diccionario de persona: {persona}')

# Acceder a los elementos del diccionario
print(f'Nombre: {persona['nombre']}')
print(f'Edad: {persona.get('edad')}')
print(f'Ciudad: {persona.get('ciudad')}')

# Modificar un valor del diccionario
persona['edad'] = 35
print(f'Diccionario de persona: {persona}')

# Agregar nuevo elemento al diccionario
persona['profesion'] = 'Ingeniero'
print(f'AGREGAR Diccionario de persona: {persona}')

# Eliminar elemento del diccionario
del persona['ciudad']
print(f'ELIMINAR Diccionario de persona: {persona}')

persona.pop('profesion')
print(f'ELIMINAR POP Diccionario de persona: {persona}')

# Iterar los elementos de un diccionario (llave, valor)
# Es como el unpaking de las tuplas
for llave, valor in persona.items():
    print(f'Llave: {llave}, Valor: {valor}')

#Obtener los valores
print(f'Valores Diccionario: ')
for valor in persona.values():
    print(f'- Valor: {valor}')

#Obtener los llaves
print(f'Llaves Diccionario: ')
for valor in persona.keys():
    print(f'- Valor: {llave}')
