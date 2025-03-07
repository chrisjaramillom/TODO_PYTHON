print('***COMBINACIÓN LISTAS Y TUPLAS***')

# Definir una lista que almacena tuplas
productos = [
    ('P001', 'Camiseta', 20.00),
    ('P002', 'Jean', 30.00),
    ('P003', 'Zapatos', 10.50),
]

# Imprimir la informació de cada producto
# y ademas calculamos el precio total
precio_total = 0.0
print('\nInformación de los productos: ')
for producto in productos:
    id, descripcion, precio = producto # Unpacking
    print(f'Producto Id: {id}, descripción: {descripcion}, precio: {precio:.2f}')
    precio_total += precio # o si no está desempaquetado usamos producto[2]

print(f'PRecio TOTAL: $ {precio_total} USD')