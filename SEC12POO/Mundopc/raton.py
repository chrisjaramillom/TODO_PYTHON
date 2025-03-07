#Clase Raton (Hijo)
from dispositivo_entrada import Dispositivo_Entrada

class Raton(Dispositivo_Entrada):
    contador_ratones = 0

    def __init__(self, tipo_entrada, marca):
        Raton.contador_ratones += 1
        self._id_raton = Raton.contador_ratones
        super().__init__(tipo_entrada, marca)

    def __str__(self):
        return f'Raton ID: {self._id_raton}, {super().__str__()}'

# Código Principal
if __name__ == '__main__':
    raton1 = Raton('USB', 'HP')
    print(raton1)
    raton2 = Raton('Bluetooth', 'Dell')
    print(raton2)
    raton3 = Raton('USB', 'Logitech')
    print(raton3)
    raton4 = Raton('Bluetooth', 'MSI')
    print(raton4)