print('***Devolución varios valores de una función***')

#Definición de una función
def personal_mayus(nombre, apellido, edad):
    print(f'Esta función regresa varios valores (tupla)')
    return nombre.upper(), apellido.upper(), edad

#Programa Principal
nombre, apellido, edad = personal_mayus('sandra', 'jaramillo', 49)
print(f'Resultado persona: nombre = {nombre}, apellido = {apellido}, edad = {edad}')

# En el resultado se puede ver que todos los valores se han cambiado a mayúsculas y los carga e imprime