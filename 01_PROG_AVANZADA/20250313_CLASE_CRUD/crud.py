import json
import os
 
FILE_PATH = 'data.json'
 
 
class CRUD:
    def __init__(self, file_name = FILE_PATH):
        self.file_name = file_name
        self._initialize_file()
   
    def _initialize_file(self):
        """Crear el archivo JSON caso no exista"""
        if not os.path.exists(self.file_name):
            self.save_data([])
   
    # Metodos Auxiliares
    def load_data(self):
        """Cargar los datos del archivo"""
        with open(self.file_name, 'r') as file:
            return json.load(file)
   
    def save_data(self, data):
        """Guardar los datos en el archivo"""
        with open(self.file_name, 'w') as file:
            json.dump(data, file, indent=4)
 
    # Métodos CRUD
    def create_data(self, data):
        """Crear un nuevo registro"""
        data = self.load_data()
        data.append(data)
        self.save_data(data)
   
    def read_data(self):
        """Leer todos los registros"""
        return self.load_data()
   
    def update_data(self, index, new_data):
        """Actualizar un registro"""
        data = self.load_data()
        if 0 <= index < len(data):
            data[index] = new_data
            self.save_data(data)
            return True
        return False
   
    def delete_data(self, index):
        """Eliminar un registro"""
        data = self.load_data()
        if 0 <= index < len(data):
            data.pop(index)
            self.save_data(data)
            return True
        return False
 
 
 # Instanciamos la clase CRUD
crud = CRUD()   # Se crea el archivo data.json si no existe

# Ejemplos de uso
crud.create_data({'name': 'Juan', 'age': 25})
crud.create_data({'name': 'Ana', 'age': 30})
crud.create_data({'name': 'Luis', 'age': 40})

print(crud.read_data())  # [{'name': 'Juan', 'age': 25}, {'name': 'Ana', 'age': 30}, {'name': 'Luis', 'age': 40}]
crud.update_data(1, {'name': 'Ana', 'age': 31})
print(crud.read_data())  # [{'name': 'Juan', 'age': 25}, {'name': 'Ana', 'age': 31}, {'name': 'Luis', 'age': 40}]

# Ejemplo de lectura
print(crud.read_data())  # [{'name': 'Juan', 'age': 25}, {'name': 'Ana', 'age': 31}, {'name': 'Luis', 'age': 40}]
crud.delete_data(1) # Eliminamos el registro en la posición 1
print(crud.read_data())  # [{'name': 'Juan', 'age': 25}, {'name': 'Luis', 'age': 40}]
crud.delete_data(10)  # Índice fuera de rango
print(crud.read_data())  # [{'name': 'Juan', 'age': 25}, {'name': 'Luis', 'age': 40}]
crud.delete_data(1.5)  # Índice inválido
print(crud.read_data())  # [{'name': 'Juan', 'age': 25}, {'name': 'Luis', 'age': 40}]

# Ejemplo de error al cargar el archivo
os.remove('data.json')  # Eliminamos el archivo data.json
print(crud.read_data())  # []  # Retorna una lista vacía
