print('***SISTEMA DE PRESTAMO DE LIBROS***')

DISTANCIA_PERMITIDA = 3
credencial = input('Tiene Credencial de la biblioteca (Si / No): ')
distancia = int(input('A cuantos kilóletros vives de la biblioteca: '))

es_elegible_prestamo = (credencial.strip().lower() == 'si'
                         or distancia <= 3)

print(f'\nEl préstamo a un libro es: {es_elegible_prestamo} ')