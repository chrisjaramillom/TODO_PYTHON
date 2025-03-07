print('*** INVENTARIO ***')

# Definimos una lista y dentro de esa lista, diccionarios para cada producto
#Variables
inventario = []
salir = False
contador = 0

while not salir:
    print(f'''\n** Menú Principal INVENTARIO **
    1. Agregar Producto
    2. Buscar Producto por Id
    3. Eliminar Producto
    4. Imprimir lista de inventario
    5. SALIR
    ''')
    try:
        opcion = int(input('Seleccione una opción: '))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        continue

    if opcion == 1:
        contador += 1
        print('\nIngresa los valores del producto:')
        nombre = input('Nombre: ')
        try:
            precio = float(input('Precio:.2f '))
            cantidad = int(input('Cantidad: '))
        except ValueError:
            print("Precio y cantidad deben ser valores numéricos.")
            contador -= 1
            continue
        # Creamos diccionario con el detalle del producto
        producto = {'id': contador, 'nombre': nombre, 'precio': precio, 'cantidad': cantidad}
        inventario.append(producto)
        print(f"Producto agregado con ID: {contador}")

    elif opcion == 2:
        try:
            id_buscar = int(input('\nIngrese el ID del producto a buscar: '))
        except ValueError:
            print("El ID debe ser un número.")
            continue
        producto_encontrado = next((p for p in inventario if p.get('id') == id_buscar), None)
        if producto_encontrado:
            print('\nInformación del producto encontrado:')
            print(f'''Id: {producto_encontrado.get('id')}
                Nombre: {producto_encontrado.get('nombre')}
                Precio: {producto_encontrado.get('precio')}
                Cantidad: {producto_encontrado.get('cantidad')}''')
        else:
            print("El ID ingresado no se encontró.")

    elif opcion == 3:
        try:
            id_eliminar = int(input('\nIngrese el ID del producto a eliminar: '))
        except ValueError:
            print("El ID debe ser un número.")
            continue
        producto_encontrado = next((p for p in inventario if p.get('id') == id_eliminar), None)
        if producto_encontrado:
            inventario.remove(producto_encontrado)
            print("Producto eliminado correctamente.")
        else:
            print("El ID ingresado no se encontró.")

    elif opcion == 4:
        if inventario:
            print(f'\n** LISTA DE INVENTARIO **')
            for lista in inventario:
                print(f'''Id: {lista.get('id')}
                Nombre: {lista.get('nombre')}
                Precio: {lista.get('precio')}
                Cantidad: {lista.get('cantidad')}\n''')
        else:
            print("El inventario está vacío.")

    elif opcion == 5:
        print("Saliendo del sistema...")
        salir = True

    else:
        print("Opción no válida, intente nuevamente.")
