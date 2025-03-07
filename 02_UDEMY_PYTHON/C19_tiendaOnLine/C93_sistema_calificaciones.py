print('***SISTEMA DE CALIFICACIONES***')

calificacion = float(input('Ingrese la calificación del estudiante: '))

if 10.0 >= calificacion >= 9.0:
    calif = 'A'
elif 9.0 > calificacion >= 8.0:
    calif = 'B'
elif 8.0 > calificacion >= 7.0:
    calif = 'C'
elif 7.0 > calificacion >= 6.0:
    calif = 'D'
elif 6.0 > calificacion >= 0.0:
    calif = 'F'
else:
    calif = 'Desconocida'

print(f'El estudiante que tiene una calificación de: {calificacion} equivale a: {calif}')