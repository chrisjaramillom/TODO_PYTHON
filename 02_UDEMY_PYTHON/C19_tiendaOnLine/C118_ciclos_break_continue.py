# Ejemplos de los ciclos break y continue
# el ciclo break rompe con el bucle while en el primer ejemplo
# el ciclo continue permite continuar a pesar que no cumpla con la condición, segundo ejemplo

# Ejemplo con break

print('Ciclo break')
for numero in range (1, 10):
    if numero % 2 == 0:  # número par
        print(numero)
        break # Salimos del ciclo inmediatamente

# Ejemplo con continue
print('\nPalabra continue: ')
for numero in range (1, 10):
    if numero % 2 == 1:  # número impar
        continue
    print(numero) # número par
    print('Prueba de impresión')