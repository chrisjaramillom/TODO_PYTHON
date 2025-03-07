# Manejo de SETS o CONJUNTOS

print('***Manejo de Sets o Conjuntos***')

#Crear un conjunto
mi_set = {1,10,3,4,5,4,3,3,3,3,6,7,8,10}
print(mi_set)

#Agregar elementos al SET
mi_set.add(9)
mi_set.add(2)
print(mi_set)

#Agregar elementos ya existente al SET
mi_set.add(9)
mi_set.add(2)
print(mi_set)
# No se duplican valores, solo acepta valores únicos

#Eliminar elementos
mi_set.remove(9)
mi_set.remove(2)
print(mi_set)

#Iterar elementos del set
for elemento in mi_set:
    print(elemento, end=', ')

#Comprobar si un elemento existe en el Set
print(f'\nExiste el valor de 1 en el set? {100 in mi_set}')

#Obtener la logitud del set o largo
print(f'\nLa cantidad de elementos en el SET es de: {len(mi_set)}')