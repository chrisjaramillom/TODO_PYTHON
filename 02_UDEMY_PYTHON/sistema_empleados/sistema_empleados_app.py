from empleado import Empleado
from empresa import Empresa

print('*** Sistema de Empleados ***')

# Crear una instancia de una empresa
empresa1 = Empresa('Global Mentoring')
empresa2 = Empresa('GADMUR')

# Contratar algunos empleados
empresa1.contratar_empleado('Juan', 'Ventas')
empresa1.contratar_empleado('María', 'Marketing')
empresa1.contratar_empleado('Pedro', 'Ventas')
empresa1.contratar_empleado('Ana', 'Recursos Humanos')

empresa2.contratar_empleado('Luis', 'Ventas')
empresa2.contratar_empleado('Laura', 'Marketing')
empresa2.contratar_empleado('Carlos', 'Ventas')

# Obtener el total global de empleados
total_global = Empleado.obtener_total_empleados()
print(f'\nTotal global de empleados: {total_global}')

# Obtener el número de empleados por empresa
print(f'Total de empleados en Global Mentoring: {empresa1.obtener_numero_empleados()}')
print(f'Total de empleados en GADMUR: {empresa2.obtener_numero_empleados()}')

# Obtener el número de empleados en el departamento de ventas de la empresa
print(f'\nEmpleados en el departamento de Ventas en Global Mentoring: {empresa1.obtener_numero_empleados_departamento("Ventas")}')

# Mostrar todos los empleados de la empresa
empresa1.obtener_total_empleados()
empresa2.obtener_total_empleados()

nom_empresa = input('\nIngrese el nombre de la empresa: ')
if nom_empresa.lower() == empresa1.nombre.lower():    
    empresa1.obtener_total_empleados()
elif nom_empresa.lower() == empresa2.nombre.lower():
    empresa2.obtener_total_empleados() 
else:
    print('Empresa no encontrada')  # Mensaje de error

