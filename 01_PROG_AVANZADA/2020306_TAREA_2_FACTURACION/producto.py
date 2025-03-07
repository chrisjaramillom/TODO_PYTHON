class Producto:
    def __init__(self, codigo, nombre, precio):
        """Inicializa un producto con código, nombre y precio."""
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        """Representación en cadena del producto."""
        return f"[{self.codigo}] {self.nombre} - ${self.precio:.2f}"
