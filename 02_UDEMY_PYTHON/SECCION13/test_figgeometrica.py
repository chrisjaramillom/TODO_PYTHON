from cuadrado import Cuadrado
from color import Color
from cuadrados import Rectangulo

print ("Creación Objeto CUADRADO".center(50, '-'))
cuadrado1 = Cuadrado(ancho = 4, color = 'Rojo')
#cuadrado1.alto = 10
#cuadrado1.ancho = 10
print(cuadrado1.ancho)
print(cuadrado1.alto)
print(cuadrado1.color)
print(f'Calculo del área: {cuadrado1.calcular_area()}')

print(cuadrado1)

print ("Creación Objeto RECTANGULO".center(50, '*'))
rectangulo1 = Rectangulo(alto = 8, ancho = 6, color = 'Azul')
rectangulo1.alto = 20
print(rectangulo1.area())
print(rectangulo1)
