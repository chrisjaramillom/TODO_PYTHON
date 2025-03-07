# Realizar un programa que el usuario ingresa la cantidad de calificaciones
# y se saca el promedio de las mismas

print('CUADRO DE CALIFICACIONES Y PROMEDIO')

calificaciones = []
suma_califica = 0.0
prom = 0.0

# Ingresa número de calificaciones
num_calificaciones = int(input('Ingrese el número de calificaciones:'))

for i in range(num_calificaciones):
    calificacion = float(input(f'Ingrese la calificación {i+1}: '))
    calificaciones.append(calificacion)
    # suma_califica = suma_califica + calificaciones[i] # en vez de la línea

suma_califica = sum(calificaciones)
prom = (suma_califica / num_calificaciones)

print(f'Calificaciones ingresadas son : {calificaciones}')
print(f'Suma de las calificaciones es:  {suma_califica} y el Promedio es: {prom:.2f}')
