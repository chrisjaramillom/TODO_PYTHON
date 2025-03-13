from color import Color
from figurageometrica import FiguraGeometrica
from cuadrado import Cuadrado

class Rectangulo(FiguraGeometrica, Color):
    def __init__(self, alto, ancho, color):
        FiguraGeometrica.__init__(self, alto, ancho)
        Color.__init__(self, color)
    
    def area(self):
        return self._alto * self._ancho
    
    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)} {Color.__str__(self)}'
        #return f"Rectangulo [Alto: {self._alto}, Ancho: {self._ancho}, Color: {self._color}, Área: {self.area()}]"


# Pruebas de las clases
cuadrado = Cuadrado(5, "rojo")
print(cuadrado)


rectangulo = Rectangulo(4, 6, "azul")
print(rectangulo)
