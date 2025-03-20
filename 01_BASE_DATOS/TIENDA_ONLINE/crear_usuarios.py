from conexion import get_connection

def crear_tabla_usuarios():
    """Crea la tabla en la base de datos 'tienda_online' si no existe."""
    conexion = get_connection()

    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("USE tienda_online")  # Selecciona la base de datos

            # Verifica si la tabla ya existe
            cursor.execute("SHOW TABLES LIKE 'usuarios'")
            tabla_existe = cursor.fetchone()

            if not tabla_existe:
                # Sentencia SQL para crear la tabla
                crear_tabla_sql = """
                    CREATE TABLE roles (
                        id_rol INT AUTO_INCREMENT PRIMARY KEY,
                        nombre VARCHAR(50) UNIQUE NOT NULL,
                        activo TINYINT(1) NOT NULL DEFAULT 1 -- Eliminación lógica
                    );

                    CREATE TABLE usuarios (
                        id_usuario INT AUTO_INCREMENT PRIMARY KEY,
                        nombre VARCHAR(100) NOT NULL,
                        correo VARCHAR(100) UNIQUE NOT NULL,
                        contraseña VARCHAR(255) NOT NULL,
                        id_rol INT NOT NULL,
                        activo TINYINT(1) NOT NULL DEFAULT 1, -- Eliminación lógica
                        FOREIGN KEY (id_rol) REFERENCES roles(id_rol)
                    );
                """
                cursor.execute(crear_tabla_sql)
                print("✅ Tabla 'usuarios' creada exitosamente.")
            else:
                print("⚠️ La tabla 'usuarios' ya existe.")

        except Exception as e:
            print(f"❌ Error al crear la tabla: {e}")

        finally:
            cursor.close()
            conexion.close()
            print("🔌 Conexión cerrada.")

if __name__ == "__main__":
    crear_tabla_usuarios()
