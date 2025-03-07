# Description: Clase que simula una cuenta bancaria
class Cuenta:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def retirar(self, cantidad):
        try:
            if not isinstance(cantidad, (int, float)):
                raise ValueError("La cantidad a depositar debe ser un número.")
            
            if cantidad <= 0:  # Si la cantidad es menor o igual a cero
                raise ValueError("La cantidad a retirar debe ser mayor que cero.")
            
            if cantidad > self.saldo:
                raise ValueError("Saldo insuficiente.")
            
            self.saldo -= cantidad
            print(f"Retiro exitoso. Saldo actual: {self.saldo}")

        except ValueError as e:
            print(f"Error: {e}")

    def depositar(self, cantidad):
        try:
            if not isinstance(cantidad, (int, float)):
                raise ValueError("La cantidad a depositar debe ser un número.")
            
            if cantidad <= 0:
                raise ValueError("La cantidad a depositar debe ser mayor que cero.")
            
            self.saldo += cantidad
            print(f"Deposito exitoso. Saldo actual: {self.saldo}")
        except ValueError as e:
            print(f"Error: {e}")
            

    def consultar_saldo(self):
        return self.saldo


# Prueba de Funcionamiento
print("Prueba de Funcionamiento")
print("Creando cuenta con saldo inicial de 1000")
cuenta = Cuenta("Juan", 1000)
print(f"Saldo actual: {cuenta.consultar_saldo()}")
print("Realizando retiros")
print("CASO 1 Retirando 0")
cuenta.retirar(0)
print("CASO 2 Retirando NEGATIVO")
cuenta.retirar(-100)
print("CASO 3 Retirando MAyor que el saldo")
cuenta.retirar(2000)
print("CASO 4 Retirando Normal")
cuenta.retirar(250)
print(f"Saldo actual: {cuenta.consultar_saldo()}")