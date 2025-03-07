class Aritmetica:
    def __init__(self, operando1=None, operando2=None):
        self.operando1 = operando1
        self.operando2 = operando2

    def sumar(self):
        resultado = self.operando1 + self.operando2
        print(f'Resultado suma: {resultado}')

    def restar(self):
        resultado = self.operando1 - self.operando2
        print(f'Resultado resta: {resultado}')

    def multiplicar(self):
        resultado = self.operando1 * self.operando2
        print(f'Resultado multiplicación: {resultado:.2f}')

    def dividir(self):
        resultado = self.operando1 / self.operando2
        print(f'Resultado división: {resultado:.2f}')


# Programa principal
if __name__ == '__main__':
    print('*** Ejemplo Clase Artimética ***')
    print('Objeto 1')
    aritmetica1 = Aritmetica(5, 7)
    aritmetica1.sumar()
    aritmetica1.restar()
    aritmetica1.multiplicar()
    aritmetica1.dividir()
    print()
    # Segundo objeto
    print('Objeto 2')
    aritmetica2 = Aritmetica(12, 16)
    print()
    aritmetica2.sumar()
    aritmetica2.restar()
    aritmetica2.multiplicar()
    aritmetica2.dividir()
    print()
    # Tercer objeto
    print('Objeto 3 : Solo con un parámetro')
    aritmetica3 = Aritmetica(12)
    print()
    aritmetica3.operando2 = 10
    aritmetica3.sumar()
    aritmetica3.restar()
    aritmetica3.multiplicar()
    aritmetica3.dividir()
    print()
    # Cuarto objeto
    print('Objeto 4 : Sin parámetros')
    aritmetica4 = Aritmetica()
    print()
    aritmetica4.operando1 = 2
    aritmetica4.operando2 = 3
    aritmetica4.sumar()
    aritmetica4.restar()
    aritmetica4.multiplicar()
    aritmetica4.dividir()
    # Quinto objeto
    print('Objeto 5 : Parametros al revez')
    aritmetica5 = Aritmetica(operando2=-4, operando1=1)
    print()
    aritmetica5.sumar()
    aritmetica5.restar()
    aritmetica5.multiplicar()
    aritmetica5.dividir()