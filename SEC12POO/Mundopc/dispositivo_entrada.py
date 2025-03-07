#Clase Dispositivo Entrada (Padre)
class Dispositivo_Entrada:
    #Constructor
    def __init__(self, tipo_entrada, marca):
        self._tipo_entrada = tipo_entrada
        self._marca = marca

    def __str__(self):
        return (f'Tipo de entrada: {self._tipo_entrada}, Marca: {self._marca}')

