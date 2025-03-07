# Manejo de Listas
# Crear un programa para ingresar canciones y ordenarlas alfabéticamente

print('PLAY LIST DE CANCIONES')

lista_reproduccion = []

# Agregar Canciones
agregar = input('Desea ingresar una cancion S o N:').strip().upper()
while agregar == 'S':
    cancion = input('Ingrese canción y artista separado por un guión medio:\n').strip()
    lista_reproduccion.append(cancion)
    agregar = input('\nDesea ingresar otra cancion S o N:').strip().upper()

# Ordenar la lista en orden alfabético sort de forma ascendente
print(lista_reproduccion)
lista_reproduccion.sort()
print(lista_reproduccion)
print('Lista de reproduccion en orden alfabético: ')
for cancion in lista_reproduccion:
    print(f'- {cancion}')