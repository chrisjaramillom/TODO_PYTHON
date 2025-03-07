# Formateo de cadenas

nombre = 'Chris'
edad = 48

# con la opción mas
print('Hola, me llamo ' + nombre + ' y tengo ' + str(edad) + ' años con el más')

# f-string
mensaje = f'Hola, me llamo {nombre} y tengo {edad} años con el f-string'
print(mensaje)

# método format

mensaje = 'Hola, me llamo {} y tengo {} años, con método format'.format(nombre, edad)
print(mensaje)