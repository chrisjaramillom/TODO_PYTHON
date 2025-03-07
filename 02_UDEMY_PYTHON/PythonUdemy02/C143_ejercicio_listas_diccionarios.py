print('*** INVENTARIO inventario ***')

#Definimos una lista y dentro de esa lista diccionarios para cada producto

inventario = []

salir = False
contador = 0

while not salir:
    print(f''' **Menú Principal INVENTARIO**
    1. Agregar Producto
    2. Buscar Producto por Id
    3. Eliminar Producto
    4. Imprimir lista de inventario
    5. SALIR
    ''')
    opcion = int(input('Seleccione una opción: '))
    if opcion == 1:
        contador += 1
        print('Ingresa Valores del Producto')
        nombre = input('Nombre: ')
        precio = input('Precio: ')
        cantidad = input('Cantidad: ')
        #Creamos diccionario con el detalle producto
        producto = {'id': contador, 'nombre': nombre, 'precio': precio, 'cantidad': cantidad, }
        inventario.append(producto)
    elif opcion == 2:
        id_buscar = int(input('\nIngrese el Id del producto a buscar:'))
        for producto in inventario:
            if producto.get('id') == id_buscar:
                producto_encontrado = producto
                print('Información del producto encontrado')
                print(f'''Id: {producto_encontrado.get('id')}
                Nombre: {producto_encontrado.get('nombre')}
                Precio: {producto_encontrado.get('precio')}
                Cantidad: {producto_encontrado.get('cantidad')}''')
                break
            else:
                print(f'El Id ingresado no se encontró')
    elif opcion == 3:
        id_eliminar = input('\nIngresar Id a eliminar:').strip().lower()
        for producto in inventario:
            if producto.get('id') == id_eliminar:
                del producto['id']
                break
            else:
                print(f'El Id ingresado no se encontró')
    elif opcion == 4:
        print(f'**LISTA DE inventario**\n')
        for lista in inventario:
            print(f'''
            Id: {lista.get('id')}
            Nombre: {lista.get('nombre')}
            Precio: {lista.get('precio')}
            Cantidad: {lista.get('cantidad')}''')
    elif opcion == 5:
        print('Gracias ADIOS\n')
        salir = True
    else :
        print('Opción INVALIDA\n')