class Restaurante:
    def __init__(self, nombre):
        self.nombre = nombre
        self.pedidos = []
    
    def agregar_pedido(self, pedido):
        self.pedidos.append(pedido)
    
    def mostrar_ventas(self):
        total = 0
        for pedido in self.pedidos:
            total += pedido.calcular_total()
        return f'Su total es de: {total}.2f

    def __str__(self):
        return f'Nombre: {self.nombre}, Categoria: {self.categoria}, Precio: {self.precio}'