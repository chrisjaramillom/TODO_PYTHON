print('***OPERACIONES ENTRE SETS***')

a = {1,2,3}
b = {4,5,6,2,2,2}

print(f'Set a = {a}')
print(f'Set b = {b}')
union = a|b
print(f'Union de a y b (a|b) = {union}')

interseccion = a & b
print(f'Intersección de a y b (a & b) = {interseccion}')

resta = a - b
print(f'Resta de a y b (a - b) = {resta}')