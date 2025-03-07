print('***SENTENCIA IF, ELIF y ELSE')

edad = int(input('Ingresar tu edad: '))
if edad < 14:
    print(f'Eres un niño. Tienes {edad} años')
elif edad < 18:
    print(f'Eres menor de edad, casi un adolescente. Tienes {edad} años')
elif edad < 65:
    print(f'Eres mayor de edad. Tienes {edad} años')
else:
    print(f'Eres de la tercera edad edad. Tienes {edad} años')

print('Este mensaje se imprime siempre xq está fuera del condicionante')