from conexion import get_connection

def agregar_columna_stock_minimo():
    """Agrega la columna 'stock_minimo' a la tabla 'productos' si no existe."""
    conexion = get_connection()

    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("USE tienda_online")  # Seleccionar la base de datos

            # Verificar si la columna ya existe
            cursor.execute("SHOW COLUMNS FROM productos LIKE 'stock_minimo'")
            columna_existe = cursor.fetchone()

            if not columna_existe:
                # Agregar la columna stock_minimo
                alter_sql = """
                    ALTER TABLE productos 
                    ADD COLUMN stock_minimo INT NOT NULL DEFAULT 5
                """
                cursor.execute(alter_sql)
                conexion.commit()
                print("✅ Columna 'stock_minimo' agregada correctamente a la tabla 'productos'.")
            else:
                print("⚠️ La columna 'stock_minimo' ya existe en la tabla 'productos'.")

        except Exception as e:
            print(f"❌ Error al agregar la columna 'stock_minimo': {e}")

        finally:
            cursor.close()
            conexion.close()
            print("🔌 Conexión cerrada.")

if __name__ == "__main__":
    agregar_columna_stock_minimo()