# Lo que nos permiten estas funciones con argumentos por nombres
# es ser más flexibles al momento de ejecutar una función
# ya que nos permite cargar o no argumentos que sean opcionales
# eso se define en la cabecera de la función al dar valores por defecto
# a cada parámetro ejemplo en apellido = '' y en edad = 0

print('*** Función con argumentos por nombre ***')

def imprimir_persona(nombre, apellido='', edad=0):
    print(f'Persona: nombre = {nombre}, apellido = {apellido}, edad = {edad}')

# Primero llamamos la funcion pasando los argumentos de manera posicional
imprimir_persona('Ricardo', 'Quintana', 32)

# Llamar la funcion usando argumentos por nombre
imprimir_persona(nombre='Carlos', apellido='Rojas', edad=28)

# Llamar la funcion usando argumentos por nombre, pero intercambiando el orden
imprimir_persona(edad=28, apellido='Rojas', nombre='Carlos')

# Argumentos con valor por default
imprimir_persona(nombre='Carlos')
imprimir_persona(nombre='Carlos', apellido='Rojas')
imprimir_persona(apellido='Rojas', nombre='Carlos')