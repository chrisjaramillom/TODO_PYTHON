from conexion import get_connection

def insertar_clientes():
    """Inserta clientes en la tabla 'clientes' de la base de datos 'tienda_online'."""
    conexion = get_connection()

    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("USE tienda_online")  # Seleccionar la base de datos

            # Consulta SQL para insertar clientes
            insertar_sql = """
                INSERT INTO clientes (nombre, correo, telefono, direccion, activo) 
                VALUES (%s, %s, %s, %s, %s)
            """

            # Lista de clientes a insertar
            clientes = [
                ('Juan Pérez', 'juanperez@email.com', '0987654321', 'Av. Principal 123', 1),
                ('María López', 'marialopez@email.com', '0981122334', 'Calle Secundaria 456', 1),
                ('Carlos Rodríguez', 'carlosr@email.com', '0993344556', 'Urbanización Norte 789', 1),
                ('Ana Martínez', 'anamartinez@email.com', '0977766554', 'Sector Centro 321', 1),
                ('Pedro Gómez', 'pedrogomez@email.com', '0989988776', 'Barrio Sur 654', 1)
            ]

            # Ejecutar la inserción de los clientes
            cursor.executemany(insertar_sql, clientes)

            # Confirmar los cambios
            conexion.commit()

            print(f"✅ {cursor.rowcount} clientes insertados correctamente en la tabla 'clientes'.")

        except Exception as e:
            print(f"❌ Error al insertar clientes: {e}")

        finally:
            cursor.close()
            conexion.close()
            print("🔌 Conexión cerrada.")

if __name__ == "__main__":
    insertar_clientes()