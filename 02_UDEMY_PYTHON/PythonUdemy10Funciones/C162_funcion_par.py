print('***FUNCION PARA NUMEROS PARES***')

def es_par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

# Llamar a la función
if __name__ == '__main__':
    numero = int(input('Ingrese un valor numérico: '))
    print(f'Número ingresado es par? {es_par(numero)}')
