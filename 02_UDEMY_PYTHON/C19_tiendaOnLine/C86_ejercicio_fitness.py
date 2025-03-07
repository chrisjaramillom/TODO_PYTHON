print('***EJERCICIO FITNESS***')

nombre = input('Ingresa tu nombre: ')
pasos = int(input('Ingresa los pasos caminados en el día: '))

META_PASOS_DIARIOS = 10000
CALORIAS_POR_PASO = 0.04 # Valor aproximado de Kilocalorias

calorias_quemadas = pasos * CALORIAS_POR_PASO

print(f'{nombre}')
print(f'Tu caminsate {pasos} pasos')
if pasos >= META_PASOS_DIARIOS:
    print('Por lo que COMPLETASTE TU META')
else:
    print('Por lo que NO CAMINASTE LO SUFICIENTE')

print(f'Tu quemaste el día de hoy {calorias_quemadas} kilocalorias')