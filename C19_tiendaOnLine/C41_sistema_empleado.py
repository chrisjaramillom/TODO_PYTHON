# Ejemplo de un sistema para solicitar datos

empleado_nombre = input('Ingrese el nombre completo del empleado: \n')
empleado_edad = int(input('Ingrese la edad del empleado: \n'))
empleado_salario = float(input('Ingrese el salario del empleado: \n'))
empleado_es_jefe = input('Ingrese si empleado es jefe: (Si/No)\n')

# Convertimos a tipo booleano el valor de es jefe

empleado_es_jefe = empleado_es_jefe.lower() == 'si'

# IMPRESIÓN DE LOS DATOS DEL EMPLEADO

print(f'\n DATOS DEL EMPLEADO')
print(f'Nombre: {empleado_nombre}')
print(f'Edad: {empleado_edad}')
print(f'Salario: $ {empleado_salario:.2f}') # e.2f indica que el valor es flotante y que imprima solo 2 dígitos
print(f'Es Jefe: {empleado_es_jefe}')
