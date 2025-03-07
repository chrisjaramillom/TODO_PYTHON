from libro import Libro 
class Libreria:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def buscar_libroxtitulo(self, titulo):
        encontrados_tit = []
        for libro in self.libros:
            if libro.titulo == titulo:
                encontrados_tit.append(libro)
        return encontrados_tit

    def buscar_libroxautor(self, autor):
        encontrados = []
        for libro in self.libros:
            if libro.autor == autor:
                encontrados.append(libro)
        return encontrados

    
    def listar_libros(self):
        for libro in self.libros:
            print(libro)

print("***Libreria***")
libreria1 = Libreria()
libreria1.agregar_libro(Libro("El Quijote", "Cervantes"))
libreria1.agregar_libro(Libro("El Aleph", "Borges"))
libreria1.agregar_libro(Libro("El Elefante", "Coello"))
libreria1.agregar_libro(Libro("La Abeja", "Borges"))
libreria1.agregar_libro(Libro("El Aleph", "Jaramillo"))

libreria1.listar_libros()

print ('\n BUSQUEDA DE LIBROS POR AUTOR')
lista_libros = (libreria1.buscar_libroxautor("Borges"))
for libro in lista_libros:
    print(libro)

print ('\n BUSQUEDA DE LIBROS POR TÍTULOS')
lista_libros_titulo = (libreria1.buscar_libroxtitulo("El Aleph"))
for libro in lista_libros_titulo:   
    print(libro)
