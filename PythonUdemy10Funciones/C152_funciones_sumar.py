# Ejemplo de una función que suma dos parámetros
from C153_funciones_modulos_suma import sumar


# Cuerpo del programa
# Llamado de la función sumar
if __name__ =='__main__':
    print('***FUNCIÓN SUMAR***')
    resultado_funcion = sumar(5, 6)
    print(f'Resultado función sumar: {resultado_funcion}')

resultado_funcion = sumar(-15, 16)
print(f'Resultado función sumar: {resultado_funcion}')