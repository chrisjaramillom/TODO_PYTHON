# OPERADORES BOOLEANOS

print('***OPERADORES LÓGICOS***')
cond1 = True
cond2 = False
resultado = cond1 and cond1
print('OPERADOR LÓGICO Y')
print(f'Resultado {cond1} Y {cond1}: {resultado}')

resultado = cond1 and cond2
print(f'Resultado {cond1} Y {cond2}: {resultado}')

resultado = cond2 and cond1
print(f'Resultado {cond2} Y {cond1}: {resultado}')

resultado = cond2 and cond2
print(f'Resultado {cond2} Y {cond2}: {resultado}')

print('\nOPERADOR LÓGICO O')
resultado = cond1 or cond1
print(f'Resultado {cond1} O {cond1}: {resultado}')

resultado = cond1 or cond2
print(f'Resultado {cond1} O {cond2}: {resultado}')

resultado = cond2 or cond1
print(f'Resultado {cond2} O {cond1}: {resultado}')

resultado = cond2 or cond2
print(f'Resultado {cond2} O {cond2}: {resultado}')

print('\nOPERADOR LÓGICO NOT')
resultado = not cond1
print(f'Resultado not {cond1}: {resultado}')

resultado = not cond2
print(f'Resultado not {cond2}: {resultado}')

print('\nEJEMPLO OPERADOR LÓGICO NOT')
nombre = ''
es_cadena_vacia = not nombre
print(f'Variable está vácia? : {es_cadena_vacia}')

nombre = 'Hola'
es_cadena_vacia = not nombre
print(f'Variable está vácia? : {es_cadena_vacia}')

# Si una variable no tiene valor asignado
variable = None
variable_sin_valor = not variable
print(f'Variable SIN valor? : {variable_sin_valor}')

variable = 10
variable_sin_valor = not variable
print(f'Variable SIN valor? : {variable_sin_valor}')

# OPERADOR NOT FUERA DE RANGO
# Reviar si un dato ingresado por el usuario está dentro o fuera del rango

dato = int(input('Ingrese un número entero: '))
esta_dentro_rango = 1 <= dato <= 10
print(f'Variable está DENTRO del rango entre 1 y 10: {esta_dentro_rango}')

esta_dentro_rango = not(1 <= dato <= 10)
print(f'Variable está FUERA del rango entre 1 y 10: {esta_dentro_rango}')