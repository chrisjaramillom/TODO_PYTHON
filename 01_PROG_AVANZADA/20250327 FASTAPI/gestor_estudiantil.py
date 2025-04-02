import sqlite3

DB_NAME = "estudiantes.db"

class GestorEstudiantes:
    def __init__(self, db_name=DB_NAME):
        self.db_name = db_name
        self.crear_tabla()

    def conectar(self):
        return sqlite3.connect(self.db_name)

    def crear_tabla(self):
        """Crea la tabla de estudiantes si no existe"""
        with self.conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS estudiantes (
                    codigo TEXT PRIMARY KEY,
                    nombre TEXT NOT NULL,
                    apellido TEXT NOT NULL,
                    correo TEXT NOT NULL
                )
            """)
            conn.commit()

    def existe_codigo(self, codigo):
        """Verifica si un estudiante con ese código ya existe"""
        with self.conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT 1 FROM estudiantes WHERE codigo = ?", (codigo,))
            return cursor.fetchone() is not None

    def insertar_estudiante(self, codigo, nombre, apellido, correo):
        """Insertar un nuevo estudiante"""
        if self.existe_codigo(codigo):
            print(f"⚠️ El código '{codigo}' ya está registrado. Usa otro.")
            return
        with self.conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO estudiantes (codigo, nombre, apellido, correo)
                VALUES (?, ?, ?, ?)
            """, (codigo, nombre, apellido, correo))
            conn.commit()
            print("✅ Estudiante agregado exitosamente.")


    def mostrar_estudiantes(self):
        """Mostrar todos los estudiantes"""
        with self.conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM estudiantes")
            estudiantes = cursor.fetchall()
            if estudiantes:
                print("\n📋 Listado de Estudiantes:")
                for est in estudiantes:
                    print(f"Código: {est[0]}, Nombre: {est[1]} {est[2]}, Correo: {est[3]}")
            else:
                print("⚠️ No hay estudiantes registrados.")

    def actualizar_estudiante(self, codigo, nuevo_nombre, nuevo_apellido, nuevo_correo):
        """Actualizar estudiante (sin cambiar código)"""
        with self.conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE estudiantes
                SET nombre = ?, apellido = ?, correo = ?
                WHERE codigo = ?
            """, (nuevo_nombre, nuevo_apellido, nuevo_correo, codigo))
            conn.commit()
            if cursor.rowcount:
                print("✅ Estudiante actualizado correctamente.")
            else:
                print("⚠️ Código no encontrado.")

    def eliminar_estudiante(self, codigo):
        """Eliminar estudiante por código"""
        with self.conectar() as conn:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM estudiantes WHERE codigo = ?", (codigo,))
            conn.commit()
            if cursor.rowcount:
                print("🗑️ Estudiante eliminado.")
            else:
                print("⚠️ Código no encontrado.")


# ================== MENÚ INTERACTIVO ==================
if __name__ == "__main__":
    gestor = GestorEstudiantes()

    while True:
        print("\n=== GESTOR DE ESTUDIANTES ===")
        print("1. Insertar nuevo estudiante")
        print("2. Mostrar todos los estudiantes")
        print("3. Actualizar estudiante")
        print("4. Eliminar estudiante")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            codigo = input("Código: ")
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            correo = input("Correo: ")
            gestor.insertar_estudiante(codigo, nombre, apellido, correo)

        elif opcion == "2":
            gestor.mostrar_estudiantes()

        elif opcion == "3":
            print("\n📋 Estudiantes registrados:")
            gestor.mostrar_estudiantes()

            codigo = input("\nIngrese el código del estudiante a actualizar: ")
            nuevo_nombre = input("Nuevo nombre: ")
            nuevo_apellido = input("Nuevo apellido: ")
            nuevo_correo = input("Nuevo correo: ")
            gestor.actualizar_estudiante(codigo, nuevo_nombre, nuevo_apellido, nuevo_correo)


        elif opcion == "4":
            codigo = input("Código del estudiante a eliminar: ")
            gestor.eliminar_estudiante(codigo)

        elif opcion == "5":
            print("👋 Saliendo del sistema...")
            break

        else:
            print("❌ Opción inválida. Intenta de nuevo.")
