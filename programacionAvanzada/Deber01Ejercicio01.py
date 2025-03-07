# Definimos la función que cuenta la cantidad de veces que aparece una palabra específica

def contar_palabra(frases, palabra):
    """
    Descripión de la FUNCIÓN
    Cuenta cuántas veces aparece una palabra específica en una lista de frases,
    sin importar mayúsculas o minúsculas.
    
    :param frases: Lista de frases (lista de strings)
    :param palabra: Palabra a contar (string)
    :return: Número de veces que aparece la palabra en las frases (int)
    """
    total_ocurrencias = 0  # Inicializamos el contador en 0
    palabra = palabra.lower()  # Convertimos la palabra a minúsculas para comparación
    
    for frase in frases:  # Recorremos cada frase en la lista de frases
        palabras = frase.lower().split()  # Convertimos la frase a minúsculas y la dividimos en palabras
        ocurrencias = palabras.count(palabra)  # Contamos cuántas veces aparece la palabra en la frase ya cargada
        total_ocurrencias += ocurrencias  # Sumamos al total de ocurrencias
    
    return total_ocurrencias  # Retornamos el número total de ocurrencias

# Creamos una lista llamada "frase" con cuatro elementos de tipo texto
frase = [
    "Python es un lenguaje muy popular",  # Primera frase
    "Me encanta programar en Python",     # Segunda frase
    "Aprender Python es divertido",       # Tercera frase
    "El lenguaje Python es muy versátil, python python python"  # Cuarta frase
]
# Agregamops dos frases adicionales a la lista
frase.append("Esta es la primera frase python    python.")
frase.append("  Esta es la segunda frase.")

# Ejemplo de uso
resultado = contar_palabra(frase, "python")

# Imprimimos el resultado en pantalla
print(f"La palabra 'Python' aparece {resultado} veces.")