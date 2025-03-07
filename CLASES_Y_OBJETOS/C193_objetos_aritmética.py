# Definicion de una clase
class Aritmetica:
    #  Constructor del Objeto
    def __init__(self, operador1, operador2):
        # Creamos los atributos de la clase
        self.operador1 = operador1
        self.operador2 = operador2

    def sumar(self):
        print(f'''Suma: 
        {self.operador1} + {self.operador2} = {self.operador1 + self.operador2}''')

# Creacion de objetos
if __name__ == '__main__':
    # Creacion de un primer objeto
    operadores = Aritmetica(5.5, 6.6)  # Crea un objeto vacio en memoria
    operadores.sumar()
    print(f'Dir. mem persona1: {id(persona1)}')
    print(f'Dir. mem persona1: {hex(id(persona1))}')

    # Creamos un segundo objeto
    persona2 = Persona('Ian', 'Sánchez') # Crea un objeto vacio en memoria
    #persona2.inicializar_persona('Ian', 'Sánchez')
    persona2.mostrar_persona()