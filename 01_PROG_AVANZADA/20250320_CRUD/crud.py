#Ejemplo de un CRUD

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
        try:
            with open(self.file_name, 'w') as file:
                json.dump(data, file, indent=4)
        except (Exception, TypeError) as e:
            print(f'Error al guardar los datos: {e}')
 
    # Métodos CRUD
    def create_data(self, new_data):
        """Crear un nuevo registro"""
        existing_data  = self.load_data()
        existing_data.append(new_data)
        self.save_data(existing_data )
   
    def read_data(self):
        """Leer todos los registros"""
        return self.load_data()
   
    def update_data(self, index, new_data):
        """Actualizar un registro"""
        data = self.load_data()
        if 0 <= index < len(data):
            ci_original = data[index]['CI']
            updated_data = {"CI": ci_original ,"nombre": new_data["nombre"],"apellido": new_data["apellido"],"email": new_data["email"]}
            data[index] = updated_data
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
   
 
# Ejemplo de uso
if __name__ == '__main__':
    crud = CRUD()
 
    while True:
        print("\n=== MENU CRUD JSON ===")
        print("1. Crear nuevo registro")
        print("2. Leer registros")
        print("3. Actualizar registro")
        print("4. Eliminar registro")
        print("5. Salir")
        option = input("Seleccione una opción: ")
 
        if option == '1':
            ci = input("Ingrese CI: ")
            nombre = input("Ingrese Nombre: ")
            apellido = input("Ingrese Apellido: ")
            email = input("Ingrese el e-mail: ")
            crud.create_data({'CI': ci, 'nombre': nombre, 'apellido': apellido, 'email': email})
            print("Registro creado con éxito")
       
        elif option == '2':
            print("\n Registros:")
            data = crud.read_data()
            for llaves, valor in enumerate(data):
                print(f"{llaves}: {valor}")
       
        elif option == '3':
            print("\n Actualizar registro:")
            data = crud.read_data()
            if not data:
                print("No hay registros para actualizar")
                continue
            print("\n Registros actuales:")
            for llaves, valor in enumerate(data):
                print(f"{llaves}: {valor}")
            index = int(input("Ingrese el índice del registro a actualizar: "))
            nombre = input("Ingrese el nuevo Nombre: ")
            apellido = input("Ingrese el nuevo Apellido: ")
            email = input("Ingrese el nuevo E-mail: ")
            if crud.update_data(index, { 'nombre': nombre, 'apellido': apellido , 'email': email}):
                print("Registro actualizado con éxito")
            else:
                print("Índice inválido")
 
        elif option == '4':
            print("\n Eliminar registro:")
            data = crud.read_data()
            if not data:
                print("No hay registros para eliminar")
                continue
            print("\n Registros actuales:")
            for llaves, valor in enumerate(data):
                print(f"{llaves}: {valor}")
            index = int(input("Ingrese el índice del registro a eliminar: "))
            if crud.delete(index):
                print("Registro actualizado con éxito")
            else:
                print("Índice inválido")
       
        elif option == '5':
            print("Saliendo...")
            break
 
        else:
            print("Opción inválida")
 
 