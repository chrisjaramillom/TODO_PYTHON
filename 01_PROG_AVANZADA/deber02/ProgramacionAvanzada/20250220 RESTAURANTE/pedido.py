from plato import Plato

class Pedido(Plato):
    def __init__(self, nombre, precio, cantidad):
        super().__init__(nombre, precio)
        self.cantidad = cantidad
    
    def agregar_plato(self, plato):
        self.platos.append(plato)
        
    def __str__(self):
        return f'{self.nombre} - $ {self.precio} x {self.cantidad} = $ {self.precio * self.cantidad}'
    
    #Funcion para calcular el total de la orden
    def calcular_total(self):
        return sum(self.precio * self.cantidad)
    
# Programa Principal
if __name__ == "__main__":

    plato

    # Crear 3 pedidos   para el pedido 1
    pedido01 = Pedido('Chugchucara', 5.99, 2)
    pedido02 = Pedido('Ceviche', 7.99, 3)
    pedido03 = Pedido('Seco de Chivo',8.99, 4)

    print ("CREACIÓN DE PLATOS".center(50, '-'))
    print('pedido 01')
    print(pedido01)
    print('pedido 02')
    print(pedido02)
    print('pedido 03')
    print(pedido03)
    
    
