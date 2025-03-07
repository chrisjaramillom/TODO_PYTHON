print('***DESEMPAQUETADO DE TUPLAS***')

producto = ('P001', 'Camisa', 20.00)

#Desempaquetar es asignar nombre a cada valor de una tupla
id, descripcion, precio = producto

# Imprimir valores
print(f'Tupla completa: {producto}')

#Valores independientes ya desempaquetados
print(f'Producto Id: {id}, descripción: {descripcion}, precio: {precio:.2f}')