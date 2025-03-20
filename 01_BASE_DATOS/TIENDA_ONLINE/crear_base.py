from conexion import get_connection

def crear_base_datos():
    """Crea la base de datos tienda_online si no existe."""
    conexion = get_connection()

    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("SHOW DATABASES")
            bases_de_datos = [db[0] for db in cursor.fetchall()]

            if "tienda_online" not in bases_de_datos:
                cursor.execute("CREATE DATABASE tienda_online")
                print("✅ Base de datos 'tienda_online' creada exitosamente.")
            else:
                print("⚠️ La base de datos 'tienda_online' ya existe.")

        except Exception as e:
            print(f"❌ Error al crear la base de datos: {e}")

        finally:
            cursor.close()
            conexion.close()
            print("🔌 Conexión cerrada.")

if __name__ == "__main__":
    crear_base_datos()
