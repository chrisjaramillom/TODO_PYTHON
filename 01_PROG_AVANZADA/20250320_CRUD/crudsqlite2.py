import sqlite3
 
DB_NAME = "data.db"
 
 
class CRUDSQLite:
    def __init__(self, db_name = DB_NAME):
        self.db_name = db_name
        self.create_table()
 
    def connect(self):
        return sqlite3.connect(self.db_name)
   
    def create_table(self):
        """Crear la tabla si no existe"""
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS entries (
                           id INTEGER PRIMARY KEY AUTOINCREMENT,
                           CI TEXT UNIQUE,
                           nombre TEXT,
                           apellido TEXT,
                           email TEXT
                )          
            """)
            conn.commit()
   
    # Métodos CRUD
    def create_data(self, ci, nombre, apellido, email):
        """Crear un nuevo registro"""
        try:
            with self.connect() as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO entries (CI, nombre, apellido, email) VALUES (?, ?, ?, ?)",
                               (ci, nombre, apellido, email))
                conn.commit()
 
        except sqlite3.IntegrityError:
            print(f"El CI {ci} ya existe")
   
    def read_data(self):
        """Leer todos los registros"""
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM entries")
            return cursor.fetchall()
   
    def update_data(self, entry_id, nombre, apellido, email):
        """Actualizar un registro"""
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("UPDATE entries SET nombre = ?, apellido = ?, email = ? WHERE id = ?",
                           (nombre, apellido, email, entry_id))
            conn.commit()
            return True
 
    def delete_data(self, entry_id):
        """Eliminar un registro"""
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM entries WHERE id = ?", (entry_id,))
            conn.commit()
            return True
   
 
# ========= MENU ITERATIVO =========
if __name__ == '__main__':
    crud = CRUDSQLite()
 
    while True:
        print("\n=== MENU CRUD SQLITE ===")
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
            crud.create_data(ci, nombre, apellido, email)
            print("Registro creado con éxito")
       
        elif option == '2':
            print("\n Registros:")
            data = crud.read_data()
            for row in data:
                print(f"ID: {row[0]} - CI: {row[1]} - Nombre: {row[2]} - Apellido: {row[3]} - E-mail: {row[4]}")
       
        elif option == '3':
            print("\n Actualizar registro:")
            data = crud.read_data()
            if not data:
                print("No hay registros para actualizar")
                continue
            print("\n Registros actuales:")
            for row in data:
                print(f"ID: {row[0]} - CI: {row[1]} - Nombre: {row[2]} - Apellido: {row[3]} - E-mail: {row[4]}")
 
            entry_id = int(input("Ingrese el ID del registro a actualizar: "))
            nombre = input("Ingrese el nuevo Nombre: ")
            apellido = input("Ingrese el nuevo Apellido: ")
            email = input("Ingrese el nuevo E-mail: ")
            if crud.update_data(entry_id, nombre, apellido, email):
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
           
            for row in data:
                print(f"ID: {row[0]} - CI: {row[1]} - Nombre: {row[2]} - Apellido: {row[3]} - E-mail: {row[4]}")
           
            entry_id = int(input("Ingrese el índice del registro a eliminar: "))
            if crud.delete_data(entry_id):
                print("Registro eliminado con éxito")
            else:
                print("Índice inválido")
       
        elif option == '5':
            print("Saliendo...")
            break
 
        else:
            print("Opción inválida")