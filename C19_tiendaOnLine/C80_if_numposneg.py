print('***SENTENCIA IF, ELIF y ELSE***')
print('***VERIFICAR SI UN NÚMERO ES NEGATIVO O POSITIVO')

numero = int(input('Ingresar el número: '))
if numero > 0:
    print(f'En número es positivo. Número evaluado es {numero}')
elif numero < 0:
    print(f'En número es negativo. Número evaluado es {numero}')
else:
    print(f'En número es CERO. Número evaluado es {numero}')

print('Este mensaje se imprime siempre xq está fuera del condicionante')