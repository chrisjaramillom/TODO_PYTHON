print('***CASA DE LOS ESPEJOS***')

anios = int(input('Ingresa tu edad: '))
miedo = input('Te da miedo los fantasmas (si/no): ')
miedo_booleano = miedo.strip().lower() == 'si'

if (not miedo_booleano) and (anios > 9):
    print('SIIII puedes entrar a la casa de los ESPEJOS')
else:
    print('NO puedes entrar a la casa de los ESPEJOS')