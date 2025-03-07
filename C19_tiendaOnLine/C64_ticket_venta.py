print('***GENERACIÓN DE FACTURA DE VENTA***')

precio_leche = round(float(input('Precio Leche: ')),2)
precio_pan = round(float(input('Precio Pan: ')),2)
precio_lechuga = round(float(input('Precio Lechuga: ')),2)
precio_platano = round(float(input('Precio Platano: ')),2)
descuento_porcen = round(float(input('Indique porcentaje de descuento: ')),2)

# Calculo del subtotal (sin impuestos)
# se calcula sumando todos los productos seleccionados por el usuario
subtotal = precio_leche + precio_pan + precio_lechuga + precio_platano

# Calculo del descuento
descuento = subtotal * descuento_porcen / 100

# Calculo de impuestos (15%)
impuesto = (subtotal - descuento) * 15 / 100

# Calculo de del total subtotal + impuesto

total = subtotal - descuento + impuesto
print(f'''
Subtotal 1: ${subtotal:.2f}
Descuento (10%): $ - {descuento:.2f} 
Subtotal 2 : ${subtotal - descuento:.2f}
Impuestos (15%): ${impuesto:.2f}
TOTAL: ${total:.2f}
''')

