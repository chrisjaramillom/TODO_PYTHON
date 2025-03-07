# Buscar subcadenas

cadena = 'Hola mundo!'
indice = cadena.find('mundo')

print(f'Indice de la subcadena mundo: {indice}')

# Obtener el índice de la subcadena Hola
indice = cadena.find('hola')
print(f'Indice de la subcadena de hola:  {indice}') # el -1 de resultado indica que la cadena no se enconbtró

# Tener presente que Python difiere de hola que Hola, es sensible a mayúsculas y minúsculas
indice = cadena.find('Hola')
print(f'Indice de la subcadena de Hola:  {indice}')