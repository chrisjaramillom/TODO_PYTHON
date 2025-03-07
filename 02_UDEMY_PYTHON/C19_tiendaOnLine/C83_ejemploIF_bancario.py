print('***SISTEMA BANCARIO***')

salir = input('Deseas salir del sistema (si/no): ').strip().lower()
salir_booleano = salir == 'si'

if not salir_booleano:
    print(f'Sigues dentro del Sistema')
else:
    print(f'Acabas de Salir del Sistema')


