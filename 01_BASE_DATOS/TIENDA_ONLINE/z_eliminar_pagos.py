from conexion import get_connection

def eliminar_tabla_pagos():
    """Elimina la tabla 'pagos' de la base de datos 'tienda_online' si existe."""
    conexion = get_connection()

    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("USE tienda_online")  # Seleccionar la base de datos

            # Eliminar la tabla pagos si existe
            eliminar_sql = "DROP TABLE IF EXISTS pagos"
            cursor.execute(eliminar_sql)
            conexion.commit()

            print("✅ La tabla 'pagos' ha sido eliminada correctamente.")

        except Exception as e:
            print(f"❌ Error al eliminar la tabla 'pagos': {e}")

        finally:
            cursor.close()
            conexion.close()
            print("🔌 Conexión cerrada.")

if __name__ == "__main__":
    eliminar_tabla_pagos()