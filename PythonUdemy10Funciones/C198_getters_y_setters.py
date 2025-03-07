# Definimos la clase coche
# Se crean los atributos protegidos, es decir un guión bajo "_" a cada atributo
# Se crean los métodos getters (para ver) y setters (para asignar)
class Coche:

    def __init__(self, marca, modelo, color):
        self._marca = marca # Atributo protegido
        self._modelo = modelo # Atributo protegido
        self._color = color # Atributo protegido

    def conducir(self):
        print(f'''Conduciendo el coche: (Datos actualizados)
        Marca: {self._marca}
        Modelo: {self._modelo}
        Color: {self._color}''')

    def get_marca(self):
        return self._marca

    def set_marca(self, marca):
        self._marca = marca

    def get_modelo(self):
        return self._modelo

    def set_modelo(self, modelo):
        self._modelo = modelo

    def get_color(self):
        return self._color

    def set_color(self, color):
        self._color = color


# Programa principal
if __name__ == '__main__':
    # Creacion de un primer coche
    coche1 = Coche('Toyota', 'Yaris', 'Azul')
    coche1.conducir()
    # Actualiza valores del Coche e imprime nuevos valores
    # No deberíamos acceder a los atributos que no sean públicos
    coche1.set_marca('Toyota Set')
    coche1.set_modelo('Yaris Set')
    coche1.set_color('Azul Set')
    coche1.conducir()