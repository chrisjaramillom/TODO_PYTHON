from libro import Libro  # Importamos la clase Libro

class Biblioteca:
    def __init__(self, nombre):
        """Inicializa una biblioteca con un nombre y una lista vacía de libros."""
        self.nombre = nombre
        self.libros = []

    def agregar_libro(self, libro):
        """Agrega un libro a la biblioteca."""
        self.libros.append(libro)
        print(f"📚 Libro '{libro.titulo}' agregado a la biblioteca '{self.nombre}'.")

    def listar_libros_disponibles(self):
        """Muestra los libros disponibles en la biblioteca."""
        print("\n📖 Libros disponibles en la biblioteca:")
        disponibles = [libro for libro in self.libros if libro.disponible]
        if disponibles:
            for libro in disponibles:
                print(libro)
        else:
            print("⚠️ No hay libros disponibles.")

    def buscar_libro(self, titulo):
        """Busca todos los libros con el título especificado."""
        libros_encontrados = [libro for libro in self.libros if libro.titulo.lower() == titulo.lower()]
        return libros_encontrados

    def buscar_libro_autor(self, autor):
        """Busca todos los libros escritos por el autor especificado."""
        libros_encontrados = [libro for libro in self.libros if libro.autor.lower() == autor.lower()]
        return libros_encontrados
