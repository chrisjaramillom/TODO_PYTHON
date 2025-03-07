# Ejercvicio de Receta

receta_nombre = input('Ingrese el nombre de la receta: \n')
receta_ingredientes = input('Ingrese los ingredientes: \n')
receta_tiempo = int(input('Ingrese el tiempo de preparación en minutos: \n'))
receta_dificultad = input('Ingrese la dificultada de esta receta (Facil, Medio, Dificil)\n')

# IMPRESIÓN DE LOS DATOS DEL EMPLEADO

print('\n-----------------------------------')
print(f' ***DATOS DE LA RECETA***')
print(f'Nombre: {receta_nombre}')
print(f'Ingredientes: {receta_ingredientes}')
print(f'Tiempo de preparación: {receta_tiempo + 60} minutos')
print(f'Dificultad: {receta_dificultad}')
