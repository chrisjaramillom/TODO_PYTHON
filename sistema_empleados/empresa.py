from empleado import Empleado

class Empresa:
    def __init__(self, nombre):  # Constructor de la clase Empresa
        self.nombre = nombre  # Nombre de la empresa
        self.empleados = []   # Empleados de la empresa

    def contratar_empleado(self, nombre, departamento):
        empleado = Empleado(nombre, departamento)  # Crear una instancia de la clase Empleado
        self.empleados.append(empleado)  # Agregar el objeto empleado a la lista de empleados

    # Método para obtener el número de empleados por departamento
    def obtener_numero_empleados_departamento(self, departamento):
        contador_empleados_por_departamento = 0
        for empleado in self.empleados:
            if empleado.departamento == departamento:  # Si el departamento del empleado es igual al departamento que se desea contar
                contador_empleados_por_departamento += 1
        return contador_empleados_por_departamento

    # Método para obtener todos los empleados de la empresa
    def obtener_total_empleados(self):
        print(f'\nLista de Empleados para la empresa: {self.nombre}')
        for empleado in self.empleados:
            print(f'''
                Empleado {empleado.id}
                Nombre: {empleado.nombre}
                Departamento: {empleado.departamento}''')
        return f'\nLista de Empleados para la empresa: {self.nombre}'

    # Método para obtener el número de empleados de la empresa
    def obtener_numero_empleados(self):
        return len(self.empleados)  # Devolver la cantidad de empleados en la lista de empleados