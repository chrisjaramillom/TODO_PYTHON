class Libro:
    def __init__(self, titulo, autor, isbn):
        """Inicializa un libro con su título, autor, ISBN y estado disponible."""
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True  # Estado del libro (True = disponible, False = prestado)

    def prestar(self):
        """Cambia el estado del libro a prestado si está disponible."""
        if self.disponible:
            self.disponible = False
            print(f"El libro '{self.titulo}' ha sido prestado.")
        else:
            print(f"El libro '{self.titulo}' ya está prestado.")

    def devolver(self):
        """Cambia el estado del libro a disponible si estaba prestado."""
        if not self.disponible:
            self.disponible = True
            print(f"El libro '{self.titulo}' ha sido devuelto.")
        else:
            print(f"El libro '{self.titulo}' ya estaba disponible.")

    def __str__(self):
        """Representación en cadena del libro."""
        estado = "Disponible" if self.disponible else "Prestado"
        return f"{self.titulo} - {self.autor} (ISBN: {self.isbn}) [{estado}]"
