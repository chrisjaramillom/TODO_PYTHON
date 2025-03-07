from figurageometrica import FiguraGeometrica
from color import Color

class Cuadrado(FiguraGeometrica, Color):
    def __init__(self, ancho, color):
        #super().__init__(ancho, ancho)
        FiguraGeometrica.__init__(self, ancho, ancho)
        Color.__init__(self, color)
        
    def calcular_area(self):
        return self.ancho * self.alto
    
    def __str__(self):
        return f'{FiguraGeometrica.__str__(self)}, {Color.__str__(self)}'
    
    

