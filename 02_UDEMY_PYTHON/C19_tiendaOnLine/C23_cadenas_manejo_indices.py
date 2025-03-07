# Manejo de indices en una cadena

cadena1 = 'Hola Mundo'
cadena2 = 'maldito'
cadena3 = 'sea'
print(cadena1)
print(cadena2 + ' '+ cadena3)

# Recueprar un caracter de nuestra cadena
cadena_primero = cadena1[5] # Recupera caracter según el índice
cadena_ultimo = cadena1[9]

# Cambiar una letra de la cadena
#cadena1[0] = 'h'   no es permitido ya que las cadenas son inmutables en una parte
# se se quiere cambiar una cadena se debe reasignar en su totalidad no solo una parte.

print(cadena_primero)
print(cadena_ultimo)
print(cadena1[9])