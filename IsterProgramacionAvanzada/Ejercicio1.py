inventario = ["manzana", "banana", "naranja"]

def mostrar_inventario():
    print("Inventario actual:")
    for i, elemento in enumerate(inventario):
        print(f"{i + 1}. {elemento}")

def agregar_elemento():
    nuevo_elemento = input("Ingrese el nombre del nuevo elemento: ")
    inventario.append(nuevo_elemento)
    print(f"Se agregó '{nuevo_elemento}' al inventario.")

def agregar_elementos_extend():
    nuevos_elementos = input("Ingrese los nombres de los nuevos elementos separados por comas: ").split(",")
    inventario.extend(nuevos_elementos)
    print(f"Se agregaron '{', '.join(nuevos_elementos)}' al inventario.")

def eliminar_elemento():
    elemento_a_eliminar = input("Ingrese el nombre del elemento a eliminar: ")
    if elemento_a_eliminar in inventario:
        inventario.remove(elemento_a_eliminar)
        print(f"Se eliminó '{elemento_a_eliminar}' del inventario.")
    else:
        print(f"No se encontró '{elemento_a_eliminar}' en el inventario.")

def insertar_elemento():
    nuevo_elemento = input("Ingrese el nombre del nuevo elemento: ")
    posicion = int(input("Ingrese la posición en la que desea insertar el elemento (empezando desde 1): ")) - 1
    if 0 <= posicion <= len(inventario):
        inventario.insert(posicion, nuevo_elemento)
        print(f"Se insertó '{nuevo_elemento}' en la posición {posicion + 1}.")
    else:
        print("Posición inválida.")

def invertir_orden():
    inventario.reverse()
    print("Se invirtió el orden de los elementos en el inventario.")

while True:
    print("\n--- Menú de Gestión de Inventario ---")
    print("1. Mostrar inventario")
    print("2. Agregar elemento")
    print("3. Agregar elementos (extend)")
    print("4. Eliminar elemento")
    print("5. Insertar elemento")
    print("6. Invertir orden")
    print("7. Salir")

    opcion = input("Ingrese el número de la opción deseada: ")

    if opcion == "1":
        mostrar_inventario()
    elif opcion == "2":
        agregar_elemento()
    elif opcion == "3":
        agregar_elementos_extend()
    elif opcion == "4":
        eliminar_elemento()
    elif opcion == "5":
        insertar_elemento()
    elif opcion == "6":
        invertir_orden()
    elif opcion == "7":
        break
    else:
        print("Opción inválida. Intente de nuevo.")