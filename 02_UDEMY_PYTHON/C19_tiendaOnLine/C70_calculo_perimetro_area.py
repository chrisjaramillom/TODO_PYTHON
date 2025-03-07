print('***CALCULO DE LA BASE Y ALTURA DE UN RECTANGULO***')

print('Ingrese los datos del rectángulo: ')
base = round(float(input('Base: ')),2)
altura = round(float(input('Altura: ')),2)

# Calculo del Area (base * altura
area = base * altura

# Calculo del Perímetro (base + altura) *2
perimetro = (base + altura) * 2

#RESPUESTA
print(f'''
RESPUESTA:
AREA: {area:.2f}
PERIMETRO: {perimetro:.2f} 
''')
