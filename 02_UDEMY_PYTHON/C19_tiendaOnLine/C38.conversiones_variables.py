# Conversión de tipos de datos o variables

# Conversión de cadena a entero

cadena = '10'
cadena_entero = int(cadena)
print(f'Valor de variable cadena: {cadena}')
print(f'Valor de variable entero: {cadena_entero}')

cadena = '3.14'
cadena_flotante = float(cadena)

print()
print(f'Valor de variable cadena: {cadena}')
print(f'Valor de variable flotante: {cadena_flotante}')

entero = 10
entero_cadena = str(entero)

print()
print(f'Valor de variable entero: {entero}')
print(f'Valor de variable cadena: {entero_cadena}')

flotante = 3.1415
flotante_cadena = str(flotante)

print()
print(f'Valor de variable flotante: {flotante}')
print(f'Valor de variable cadena: {flotante_cadena}')

# Convertir a booleano
# Tipo booleano es falso en los siguientes casos:
# Si en valor es 0, cadena vacía, o None, entonces regresa False
# Tipo booleano es verdadero en los siguientes casos:
# Si el valor es 1 o distinto de cero, si es distinto de cadena vacióa regresa True.
# y si es distinto de None o null

print()

entero = 0
booleano = bool(entero)
print(f'Entero CERO regresa: {booleano}')

cadena = ''
booleano = bool(cadena)
print(f'Cadena vacía regresa: {booleano}')

print()

entero = 1
booleano = bool(entero)
print(f'Entero diferente de CERO regresa: {booleano}')

cadena = 'T'
booleano = bool(cadena)
print(f'Cadena NO vacía regresa: {booleano}')

cadena = None
booleano = bool(cadena)
print(f'Cadena None regresa: {booleano}')