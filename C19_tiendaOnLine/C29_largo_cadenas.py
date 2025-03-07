# Largo de una cadena

cadena = 'Hola, mundo!   '
largo_cadena = len(cadena)

print(cadena)
print(largo_cadena + 15)

# ----Ejemplo de conteo de caracteres en una frase----
from collections import Counter

def contar_letras(texto):
    # Convertimos el texto a minúsculas y eliminamos los espacios
    texto_limpio = texto.strip().lower()
    # Usamos Counter para contar las letras
    conteo = Counter(texto_limpio)
    return conteo

# Ejemplo de uso
texto = "HoooooooooOOOOOOOla mundo cruel y nefasto"
resultado = contar_letras(texto)

# Mostramos el resultado
for letra, cantidad in resultado.items():
    print(f"La letra '{letra}' aparece {cantidad} vez/veces.")
