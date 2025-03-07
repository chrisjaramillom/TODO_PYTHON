# Description: Clase Biblioteca

class Biblioteca:
    def __init__(self, nombre):
        self.__nombre = nombre
        self.__libros = [] # Definimos una lista vacia para almacenar los libros

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_libros(self):
        return self.__libros

    def set_libros(self, libros):
        self.__libros = libros

    def agregar_libro(self, libro):
        self.__libros.append(libro)

    def buscar_por_autor(self, autor):
        libros_autor = []
        for libro in self.__libros:
            if libro.get_autor().lower() == autor.lower():
                libros_autor.append(libro)
        return libros_autor

    def buscar_por_genero(self, genero):
        libros_genero = []
        for libro in self.__libros:
            if libro.get_genero() == genero:
                libros_genero.append(libro)
        return libros_genero

