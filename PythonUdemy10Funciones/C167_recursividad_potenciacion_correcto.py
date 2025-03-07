print('*** POTENCIACIÓN DEL NÚMERO ***')
# Chat GPT
# Definir la función recursiva para la potenciación
def potenciacion_recursiva(base, exponente):
    # Caso base: cualquier número elevado a 0 es 1 (excepto 0^0 que es indefinido)
    if exponente == 0:
        return 1

    # Caso base para exponente negativo (manejo de fracciones)
    if exponente < 0:
        return 1 / potenciacion_recursiva(base, -exponente)

    # Caso recursivo: base^exponente = base * base^(exponente-1)
    return base * potenciacion_recursiva(base, exponente - 1)


# Programa Principal
base = int(input('Ingrese el valor de la base: '))
exponente = int(input('Ingrese el valor del exponente: '))

# Calcular la potencia
resultado = potenciacion_recursiva(base, exponente)

# Mostrar resultado
print(f'La potencia de {base} elevado a {exponente} es: {resultado}')
