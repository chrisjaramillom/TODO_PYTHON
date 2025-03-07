from producto import Producto
from cliente import Cliente
from factura import Factura

def mostrar_menu():
    """Muestra el menú de opciones disponibles en el sistema de facturación."""
    print("\n*** MENÚ DE FACTURACIÓN ***")
    print("1. Agregar productos")
    print("2. Crear cliente")
    print("3. Generar factura")
    print("4. Salir")

# --- Interacción con el usuario ---
productos_disponibles = []
factura = None

while True:
    mostrar_menu()
    opcion = input("\nSeleccione una opción (1-4): ")

    if opcion == "1":
        # Agregar productos
        pro_codigo = input("\nIngrese el código del producto: ")
        pro_nombre = input("Ingrese el nombre del producto: ")
        pro_precio = float(input("Ingrese el precio del producto: "))
        producto = Producto(pro_codigo, pro_nombre, pro_precio)
        productos_disponibles.append(producto)
        print(f"✅ Producto '{pro_nombre}' agregado al inventario.")

    elif opcion == "2":
        # Crear cliente
        cli_id= input("\nIngrese el ID del cliente: ")
        cli_nombre = input("Ingrese el nombre del cliente: ")
        cli_direccion = input("Ingrese la dirección del cliente: ")
        cliente = Cliente(cli_id, cli_nombre, cli_direccion)
        factura = Factura(cliente)  # Se crea la factura asociada al cliente
        print(f"✅ Cliente '{cli_nombre}' registrado.")

    elif opcion == "3":
        # Generar factura
        if factura is None:
            print("⚠️ Primero debe registrar un cliente antes de generar una factura.")
            continue

        print("\n📦 Productos disponibles:")
        for i, producto in enumerate(productos_disponibles, 1):
            print(f"{i}. {producto}")

        while True:
            seleccion = input("\nSeleccione un producto por número (o '0' para terminar): ")
            if seleccion == "0":
                break

            try:
                index = int(seleccion) - 1
                if 0 <= index < len(productos_disponibles):
                    cantidad = int(input(f"Ingrese la cantidad de '{productos_disponibles[index].nombre}': "))
                    factura.agregar_producto(productos_disponibles[index], cantidad)
                else:
                    print("⚠️ Número inválido. Intente nuevamente.")
            except ValueError:
                print("⚠️ Entrada inválida. Ingrese un número.")

        factura.generar_factura()

    elif opcion == "4":
        print("\n👋 Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("⚠️ Opción inválida. Intente nuevamente.")
