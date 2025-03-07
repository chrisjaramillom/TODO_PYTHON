print('***ESTACIONES DEL AÑO***')

mes = int(input('Ingresa el número del mes escogido: '))

if 1 <= mes <= 2 or mes == 12:
    estacion = 'Invierno'
elif 3 <= mes <= 5:
    estacion = 'Primavera'
elif 6 <= mes <= 8:
    estacion = 'Verano'
elif 9 <= mes <= 11:
    estacion = 'Otoño'
else:
    estacion = 'Estación Desconocida'

print(f'Estamos en {estacion}')