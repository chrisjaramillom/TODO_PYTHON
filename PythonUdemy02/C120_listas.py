# Manejo de Listas

print('Manejo de LISTAS')

mi_lista = [1, 2, 3, 4, 5]
print(mi_lista)

# Longitud de una lista
print(f'Cantidad de elementos de la lista: {len(mi_lista)}')

# Accedeer al valor almacenado en el índice 4
print(f'Accedemos al indice 4: {mi_lista[4]}')
print(f'Accedemos al último valor de la lista: {mi_lista[-1]}')

# Modificar elementos de una lista
mi_lista[0] = 10
print(mi_lista)

# Agregar nuevos elementos al final de la lista

mi_lista.append(100)
print(mi_lista)
print('Elemento 6 se agregó al final con el append\n')

mi_lista.insert(2, 100)
print(mi_lista)
print('Elemento 100 se agregó en el indice 2\n')

mi_lista.remove(100)
print(mi_lista)
print('eliminamos el primer valor ingresado como parámetro, no importa el indice, en este caso el 100\n')
# Si existen más valores iguales en otros índices NO SON ELIMINADOS

mi_lista.pop(0)
print(mi_lista)
print('eliminamos el indice de la lista, en este caso el 10')

del mi_lista[2]
print(mi_lista)
print('eliminamos el índice, en este caso el 100\n')

sublista = mi_lista[1:3] # genera una lista con los indices indicados, sin incluir el último indice
print(len(sublista))
print(f'resultado de la sublista {sublista}\n')

# Iteración de listas

print(f'\n ***ITERACIÓN DE LISTA***')

nombres = ['Karla', 'Chris', 'Giu']
for nombre in nombres:
    print(nombre)

lista_heterogenea = [100, 'Chris', True]
print()
for elemento in lista_heterogenea:
    print(elemento)

lista_heterogenea[2] = False
print(lista_heterogenea)

