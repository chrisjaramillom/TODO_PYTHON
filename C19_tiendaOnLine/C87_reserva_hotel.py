print('***EJERCICIO FITNESS***')

huesped = input('Nombre del Huesped: ')
estadia = int(input('Dias de estadía: '))
vista_mar = input('Habitación con vista al mar (si/no): ').strip().lower()

vista_mar_bool = vista_mar == 'si'

HAB_VISTA_MAR = 190.50
HAB_SIN_VISTA_MAR = 150.50

# CALCULO DEL COSTO TOTAL DE LA RESERVA
if vista_mar_bool :
    total = HAB_VISTA_MAR * estadia
    hvm = 'SI'
else:
    total = HAB_SIN_VISTA_MAR * estadia
    hvm = 'NO'

print('\n-----------DETALLE DE LA RESERVACIÓN---------------')
print(f'\nHuesped: {huesped} ')
print(f'Dias de estadía: {estadia}')
print(f'Costo total: $ {total:.2f} USD')
print(f'Habitación con vista al mar: {hvm}')