from biblioteca import Biblioteca
from libro import Libro

biblioteca = None
opcion = 0
while opcion != 6:
    print('***SISTEMA DE BIBLIOTECAS***')
    print('1. Crear biblioteca')
    print('2. Agregar libro')
    print('3. Buscar libro por autor')
    print('4. Buscar libro por género')
    print('5. Listar todos los libros')
    print('6. Salir')
    opcion = int(input('Ingrese una opción: '))
    if opcion == 1:
        nombre = input('Ingrese el nombre de la biblioteca: ')
        biblioteca = Biblioteca(nombre)
    elif opcion == 2:
        if biblioteca is None:
            print('Primero debe crear una biblioteca')
        else:
            titulo = input('Ingrese el título del libro: ')
            autor = input('Ingrese el autor del libro: ')
            genero = input('Ingrese el género del libro: ')
            libro = Libro(titulo, autor, genero)
            biblioteca.agregar_libro(libro)
    elif opcion == 3:
        if biblioteca is None:
            print('Primero debe crear una biblioteca')
        else:
            autor = input('Ingrese el autor del libro: ')
            libros_autor = biblioteca.buscar_por_autor(autor)
            for libro in libros_autor:
                print(f'Título: {libro.get_titulo()}, Autor: {libro.get_autor()}, Género: {libro.get_genero()}')
    elif opcion == 4:
        if biblioteca is None:
            print('Primero debe crear una biblioteca')
        else:
            genero = input('Ingrese el género del libro: ')
            libros_genero = biblioteca.buscar_por_genero(genero)
            for libro in libros_genero:
                print(f'Título: {libro.get_titulo()}, Autor: {libro.get_autor()}, Género: {libro.get_genero()}')
    elif opcion == 5:
        if biblioteca is None:
            print('Primero debe crear una biblioteca')
        else:
            libros = biblioteca.get_libros()
            for libro in libros:
                print(f'''\tTítulo: {libro.get_titulo()},
                \tAutor: {libro.get_autor()},
                \tGénero: {libro.get_genero()}''')
    elif opcion == 6:
        print('Saliendo del sistema...   ADIOS!!!!!!')
    else:
        print('Opción incorrecta')

