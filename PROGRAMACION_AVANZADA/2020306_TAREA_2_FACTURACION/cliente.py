class Cliente:
    def __init__(self, id_cliente, nombre, direccion):
        """Inicializa un cliente con ID, nombre y dirección."""
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.direccion = direccion

    def __str__(self):
        """Representación en cadena del cliente."""
        return f"Cliente: {self.nombre} (ID: {self.id_cliente}) - Dirección: {self.direccion}"
