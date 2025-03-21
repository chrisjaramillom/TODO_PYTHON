import sqlite3

DB_NAME = 'crud.db'

class CRUD:
    def __init__(self, db_name=DB_NAME):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self._initialize_table()
    
    def _initialize_table(self):
        """Crear la tabla si no existe"""
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS personas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                ci TEXT UNIQUE,
                nombre TEXT,
                apellido TEXT,
                mail TEXT
            )
        ''')
        self.conn.commit()

    # Métodos CRUD
    def create_data(self, ci, nombre, apellido, mail):
        self.cursor.execute('''
            INSERT INTO personas (ci, nombre, apellido, mail)
            VALUES (?, ?, ?, ?)
        ''', (ci, nombre, apellido, mail))
        self.conn.commit()
    
    def read_data(self):
        self.cursor.execute('SELECT * FROM personas')
        return self.cursor.fetchall()
    
    def update_data(self, id_, nombre, apellido, mail):
        self.cursor.execute('''
            UPDATE personas
            SET nombre = ?, apellido = ?, mail = ?
            WHERE id = ?
        ''', (nombre, apellido, mail, id_))
        self.conn.commit()
    
    def delete_data(self, id_):
        self.cursor.execute('DELETE FROM personas WHERE id = ?', (id_,))
        self.conn.commit()
    
    def close(self):
        self.conn.close()


if __name__ == '__main__':
    crud = CRUD()

    while True:
        print("\n=== MENU CRUD con SQLite3 ===")
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
            mail = input("Ingrese Mail: ")
            crud.create_data(ci, nombre, apellido, mail)
            print("Registro creado con éxito")

        elif option == '2':
            print("\n Registros:")
            data = crud.read_data()
            for row in data:
                print(f"ID {row[0]}: CI={row[1]}, Nombre={row[2]}, Apellido={row[3]}, Mail={row[4]}")

        elif option == '3':
            data = crud.read_data()
            if not data:
                print("No hay registros para actualizar")
                continue
            print("\n Registros actuales:")
            for row in data:
                print(f"ID {row[0]}: CI={row[1]}, Nombre={row[2]}, Apellido={row[3]}, Mail={row[4]}")
            try:
                id_ = int(input("Ingrese el ID del registro a actualizar: "))
                nombre = input("Ingrese el nuevo Nombre: ")
                apellido = input("Ingrese el nuevo Apellido: ")
                mail = input("Ingrese el nuevo Mail: ")
                crud.update_data(id_, nombre, apellido, mail)
                print("Registro actualizado con éxito")
            except ValueError:
                print("ID inválido")

        elif option == '4':
            data = crud.read_data()
            if not data:
                print("No hay registros para eliminar")
                continue
            print("\n Registros actuales:")
            for row in data:
                print(f"ID {row[0]}: CI={row[1]}, Nombre={row[2]}, Apellido={row[3]}, Mail={row[4]}")
            try:
                id_ = int(input("Ingrese el ID del registro a eliminar: "))
                crud.delete_data(id_)
                print("Registro eliminado con éxito")
            except ValueError:
                print("ID inválido")

        elif option == '5':
            print("Saliendo...")
            crud.close()
            break

        else:
            print("Opción inválida")
