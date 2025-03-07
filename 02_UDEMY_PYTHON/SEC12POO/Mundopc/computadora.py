
from monitor import Monitor
from raton import Raton
from teclado import Teclado


class Computadora(object):
    contador_computadoras = 0
    def __init__(self, nombre, monitor, teclado, raton):
        Computadora.contador_computadoras += 1
        self._id_computadora = Computadora.contador_computadoras
        self.nombre = nombre
        self.monitor = monitor
        self.teclado = teclado
        self.raton = raton


    def __str__(self):
        return (
            f'''
            {self.nombre}: {self._id_computadora}
                Monitor: {self.monitor}
                Teclado: {self.teclado}
                Raton: {self.raton}
            '''
        )
    
#Programa Principal
if __name__ == '__main__':
    monitor1 = Monitor('HP', 15)
    teclado1 = Teclado('USB', 'HP')
    raton1 = Raton('USB', 'HP')
    computadora1 = Computadora('HP', monitor1, teclado1, raton1)
    print(computadora1)
    
    monitor2 = Monitor('Dell', 27)
    teclado2 = Teclado('Bluetooth', 'Dell')
    raton2 = Raton('Bluetooth', 'Dell')
    computadora2 = Computadora('Dell', monitor2, teclado2, raton2)
    print (computadora2)
    
    monitor3 = Monitor('Samsung', 32)
    teclado3 = Teclado('USB', 'Samsung')
    raton3 = Raton('USB', 'Samsung')
    computadora3 = Computadora('Samsung', monitor3, teclado3, raton3)
    print(computadora3)
    
    computador4 = Computadora('Asus', monitor1, teclado2, raton3)
    print(computador4)
    