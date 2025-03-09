## Archivo: main.py
from gerente import Gerente
from programador import Programador

# Ejecutar métodos de Gerente
print('*'*50)
print('METODOS DE GERENTE')
gerente = Gerente("Rosa Melano", 45, 5000, "Recursos Humanos", 1000)
print(gerente)
print(gerente.trabajar())
print(gerente.gestionar_departamento("Cambio de Departamento"))
print(gerente.otorgar_bono())
print(gerente)
print(gerente.trabajar())
print('\n')

# Ejecutar métodos de Programador
print('*'*50)
print('METODOS DE PROGRAMADOR')
programador = Programador("Zoila Perez Sosa", 30, 3000, "Python", ["Sistema de ventas", "Chatbot AI"])
print(programador)
print(programador.trabajar())
print(programador.codificar())
print(programador.revisar_proyecto())
print(programador.trabajar())

