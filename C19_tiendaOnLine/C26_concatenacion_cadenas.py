# Concatenación de cadenas

cadena1 = 'Hola Mundo'
cadena2 = 'maldito'
cadena3 = 'sea'
cadena4 = cadena1 + cadena2 + cadena3
print(cadena4)
print(cadena2 + ' '+ cadena3)

# Utilizando el métido join
# agrega el texto a la primera cadena vacía que se define antes del join
concatenacion = ''.join(['\n\t',cadena1, ' ', cadena2, ' ', cadena3])

print(concatenacion)