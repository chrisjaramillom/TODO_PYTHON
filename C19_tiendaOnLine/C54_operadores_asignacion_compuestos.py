# OPERADORES DE ASIGNACIÓN COMPUESTOS

print('***OPERADORES DE ASIGNACIÓN COMPUESTOS***')
a, b = 10, 15
print(f'Valor Inicial a: {a}, b: {b}')

#Operador compuesto de suma +=
a += b # a = a + b
print(f'Operador a += b es: {a}')

#Operador compuesto de resta -=
a= 10 # reiniciamos el valor original de a
a -= b # a = a - b
print(f'Operador a -= b es: {a}')

#Operador compuesto de multiplicación *=
a= 10 # reiniciamos el valor original de a
a *= b # a = a * b
print(f'Operador a *= b es: {a}')

#Operador compuesto de división /=
a= 10 # reiniciamos el valor original de a
a /= b # a = a / b
print(f'Operador a /= b es: {a:.2f}')

#Operador compuesto de división entera //=
a= 10 # reiniciamos el valor original de a
a //= b # a = a // b
print(f'Operador a //= b es: {a}.   El valor entero de la división entre 10 y 15 es CERO')

#Operador compuesto de modulo o residuo %=
a= 10 # reiniciamos el valor original de a
a %= b # a = a % b
print(f'Operador a %= b es: {a}')

#Operador compuesto de potenciacion **=
a= 10 # reiniciamos el valor original de a
a **= b # a = a ** b
print(f'Operador a **= b es: {a}')