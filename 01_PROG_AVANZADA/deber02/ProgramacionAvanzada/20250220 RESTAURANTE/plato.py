class Plato:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
        
    def __str__(self):
        return f'{self.nombre} - $ {self.precio}'
    
# Programa Principal
# Crear 3 platos
plato01 = Plato('Chugchucara', 5.99)
plato02 = Plato('Ceviche', 7.99)
plato03 = Plato('Seco de Chivo',8.99)

print(plato01)
print(plato02)
print(plato03)
    
# Crear 3 platos más
plato04 = Plato('Arroz con Pollo', 6.99)
plato05 = Plato('Encebollado', 4.99)
plato06 = Plato('Fritada', 9.99)

print(plato04)
print(plato05)
print(plato06)
    
    