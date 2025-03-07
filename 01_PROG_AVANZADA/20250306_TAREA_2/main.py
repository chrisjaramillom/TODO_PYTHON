from biblioteca import Biblioteca
from libro import Libro

def mostrar_menu():
    """Muestra el menú de opciones disponibles en la biblioteca."""
    print("\n*** MENÚ DE BIBLIOTECA ***")
    print("1. Agregar un libro")
    print("2. Listar libros disponibles")
    print("3. Buscar Libro por autor")
    print("4. Buscar Libro por título")
    print("5. Prestar un libro")
    print("6. Devolver un libro")
    print("7. Salir")

# --- Interacción con el usuario ---
nombre_biblioteca = input("Ingrese el nombre de la biblioteca: ")
biblioteca = Biblioteca(nombre_biblioteca)

while True:
    mostrar_menu()
    opcion = input("\nSeleccione una opción (1-7): ")

    if opcion == "1":
        # Agregar un libro
        titulo = input("\nIngrese el título del libro: ")
        autor = input("Ingrese el autor del libro: ")
        isbn = input("Ingrese el ISBN del libro: ")
        libro = Libro(titulo, autor, isbn)
        biblioteca.agregar_libro(libro)

    elif opcion == "2":
        # Listar libros disponibles
        biblioteca.listar_libros_disponibles()

    elif opcion == "3":
        # Buscar libros por autor
        autor = input("\nIngrese el autor del libro a buscar: ")
        libros = biblioteca.buscar_libro_autor(autor)
        if libros:
            print(f"\n📚 Libros del autor '{autor}':")
            for libro in libros:
                print(libro)
        else:
            print(f"❌ No se ha encontrado ningún libro del autor '{autor}'.")

    elif opcion == "4":
        # Buscar libros por título
        titulo = input("\nIngrese el título del libro a buscar: ")
        libros = biblioteca.buscar_libro(titulo)
        if libros:
            print(f"\n📖 Libros con el título '{titulo}':")
            for libro in libros:
                print(libro)
        else:
            print(f"❌ No se ha encontrado ningún libro con el título '{titulo}'.")

    elif opcion == "5":
        # Prestar un libro
        titulo_prestamo = input("\nIngrese el título del libro a prestar: ")
        libros = biblioteca.buscar_libro(titulo_prestamo)
        if libros:
            for libro in libros:
                if libro.disponible:
                    libro.prestar()
                    break
            else:
                print(f"⚠️ Todos los ejemplares de '{titulo_prestamo}' están prestados.")
        else:
            print("❌ El libro no se encuentra en la biblioteca.")

    elif opcion == "6":
        # Devolver un libro
        titulo_devolucion = input("\nIngrese el título del libro a devolver: ")
        libros = biblioteca.buscar_libro(titulo_devolucion)
        if libros:
            for libro in libros:
                if not libro.disponible:
                    libro.devolver()
                    break
            else:
                print(f"⚠️ No hay copias de '{titulo_devolucion}' para devolver.")
        else:
            print("❌ El libro no se encuentra en la biblioteca.")

    elif opcion == "7":
        # Salir del programa
        print("\n👋 Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("⚠️ Opción inválida. Intente nuevamente.")
