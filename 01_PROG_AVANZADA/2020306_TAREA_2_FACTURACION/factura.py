from producto import Producto
from cliente import Cliente

class Factura:
    def __init__(self, cliente):
        """Inicializa una factura con un cliente y una lista de productos con cantidades."""
        self.cliente = cliente
        self.productos = []  # Lista de tuplas (producto, cantidad)

    def agregar_producto(self, producto, cantidad):
        """Agrega un producto con su cantidad a la factura."""
        self.productos.append((producto, cantidad))
        print(f"✅ Producto '{producto.nombre}' agregado con cantidad {cantidad}.")

    def generar_factura(self):
        """Genera y muestra la factura con el total a pagar."""
        print("\n📜 *** FACTURA ***")
        print(self.cliente)
        print("\nProductos comprados:")

        total = 0
        for producto, cantidad in self.productos:
            subtotal = producto.precio * cantidad
            total += subtotal
            print(f"{producto.nombre} (x{cantidad}) - ${producto.precio:.2f} c/u | Subtotal: ${subtotal:.2f}")

        print("\nTotal a pagar: ${:.2f}".format(total))
