# Métodos de Cadenas
# upper maýusculas
# lower minúsculas
# split elimina espaciones en blanco inicio y fin del texto

cadena1 = "Hola Mundo"
print(f'Cadena original: {cadena1}')

mayusculas = cadena1.upper() #convierte el texto en mayúsculas
print(f'Cadena en mayúsculas: {mayusculas}')

print(f'Cadena en mayúsculas: {mayusculas.lower()}') # convierte texto en minúsculas

cadena2 = '   Chris Jaramillo      '
print(f'Texto original:     {cadena2}')
print(f'Texto sin espacios: {cadena2.strip()}')
