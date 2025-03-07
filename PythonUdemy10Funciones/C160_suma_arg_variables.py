print('***SUMA CON ARGUENTOS VARIABLES***')

#Función de sumar que acepta argumentos variables
def sumar(*args):
    total=0
    for num in args:
        total += num
    return total

# Llamar a la función sumar
resultado = sumar(1,2,3,4,9,10, 66)
print(f'Resultado de la suma: {resultado}')