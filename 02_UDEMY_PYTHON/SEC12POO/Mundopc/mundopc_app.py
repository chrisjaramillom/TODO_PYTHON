from computadora import Computadora
from monitor import Monitor
from orden import Orden
from raton import Raton
from teclado import Teclado


print('***MUNDO PC***')

# computador 1
monitor1 = Monitor('HP', 15)
teclado1 = Teclado('USB', 'HP')
raton1 = Raton('USB', 'HP')
computadora1 = Computadora('HP', monitor1, teclado1, raton1)
print(computadora1)

#Comuptadora 2
monitor2 = Monitor('Dell', 27)
teclado2 = Teclado('Bluetooth', 'Dell')
raton2 = Raton('Bluetooth', 'Dell')
computadora2 = Computadora('Dell', monitor2, teclado2, raton2)
print (computadora2)

#Computadora 3
monitor3 = Monitor('Samsung', 32)
teclado3 = Teclado('USB', 'Samsung')
raton3 = Raton('USB', 'Samsung')
computadora3 = Computadora('Samsung', monitor3, teclado3, raton3)
print(computadora3)

#Computadora 4
computadora4 = Computadora('Asus', monitor1, teclado2, raton3)
print(computadora4)

# Crear la lista de computadores
computadoras1 = [computadora1, computadora2, computadora3, computadora4]
orden1 = Orden(computadoras1)
print(orden1)   

# Crear nueva computadora
monitor5 = Monitor('Samsung', 32)  
teclado5 = Teclado('USB', 'Samsung')
raton5 = Raton('USB', 'Samsung')
computadora5 = Computadora('Samsung', monitor5, teclado5, raton5)
print(computadora5)

# Agregar una computadora
orden1.agregar_computadora(computadora5)

# Imprimir la orden
print(orden1)
