#Clase Teclado (Hijo)
from dispositivo_entrada import Dispositivo_Entrada

class Teclado(Dispositivo_Entrada):
    contador_teclados = 0
    def __init__(self, tipo_entrada, marca):
        Teclado.contador_teclados += 1
        self._id_teclado = Teclado.contador_teclados
        super().__init__(tipo_entrada, marca)

    def __str__(self):
        return (f'Teclado ID: {self._id_teclado}, {super().__str__()}')

# Código Principal
if __name__ == '__main__':
    teclado1 = Teclado('USB', 'HP')
    print(teclado1)
    teclado2 = Teclado('Bluetooth', 'Dell')
    print(teclado2)
    teclado3 = Teclado('USB', 'Logitech')
    print(teclado3)
    teclado4 = Teclado('Bluetooth', 'MSI')
    print(teclado4)