# Definimos la función que filtra los números mayores al límite
def filtrar_numeros(numeros, limite):
    """
    Filtra los números de una lista que sean mayores a un valor límite.
    
    :param numeros: Lista de números (lista de enteros o flotantes)
    :param limite: Número límite (entero o flotante)
    :return: Lista de números mayores al límite
    """
    # return [num for num in numeros if num > limite]
    # Inicializamos una lista vacía para almacenar los números filtrados
    numeros_filtrados = []
    
    # Iteramos sobre cada número en la lista de números
    for num in numeros:
        # Verificamos si el número es mayor al límite
        if num > limite:
            # Si es mayor, lo añadimos a la lista de números filtrados
            numeros_filtrados.append(num)
    
    # Retornamos la lista con los números filtrados
    return numeros_filtrados

# Ejemplo de uso
numeros = [10, 25, 30, 5, 50, 70, 20, 100]  # Lista de números
limite = 20  # Número límite

# Llamamos a la función con la lista y el límite
lista_filtrada = filtrar_numeros(numeros, limite)

# Imprimimos el resultado en pantalla
print(f"Lista filtrada: {lista_filtrada}")