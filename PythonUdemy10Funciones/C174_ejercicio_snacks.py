print('*** Sistema de Inventarios (con funciones) ***')

# Creación de snacks
inventario = [
    {'id': 1, 'nombre': 'Papas', 'precio': 25.99},
    {'id': 2, 'nombre': 'Chupetes', 'precio': 39.99},
    {'id': 3, 'nombre': 'Chocolates', 'precio': 49.99}
]

snack_comprado = []

# Funcion para mostrar el inventario
def mostrar_snacks():
    print('--- Snacks En Venta ---')
    for producto in inventario:
        print(f'Id: {producto.get('id')}, Nombre: {producto.get('nombre')},'
              f'Precio: ${producto.get('precio')}')

def comprar_snacks():
    # pass
    print('--- Agregar Snack Comprado ---')
    id = int(input('Id: '))
    nombre = input('Nombre: ')
    precio = float(input('Precio: '))
    nuevo_producto = {'id': id, 'nombre':nombre,'precio': precio}
    inventario.append(nuevo_producto)
    print('Producto agregado al carrito de compras')
    return(nuevo_producto)

def buscar_producto_por_id():
    print('--- Inventario del Almacén ---')
    for producto in inventario:
        print(f'Id: {producto.get('id')}, Nombre: {producto.get('nombre')},'
              f'Precio: ${producto.get('precio')}')


# Programa principal
if __name__ == '__main__':
    while True:
        print(f'''\n--- Menú ---
        1. Mostrar snack
        2. Comprar Snack
        3. Mostrar ticket
        4. Salir''')
        opcion = int(input('Proporciona una opción (1-4): '))
        # Revisamos las opciones del menu
        if opcion == 1:  # Mostrar snacks
            mostrar_inventario()
        elif opcion == 2:  # comprar snacks
            carrito compras[] = agregar_producto()
        elif opcion == 3:  # Mostrat tickets
            buscar_producto_por_id()
        elif opcion == 4:  # Salir
            print('Hasta luego!')
            break
        else:
            print('Opción inválida, proporciona una opción válida')
