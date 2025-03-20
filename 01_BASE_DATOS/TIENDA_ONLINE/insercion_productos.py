from conexion import get_connection

def insertar_productos():
    """Inserta productos en la tabla 'productos' de la base de datos 'tienda_online'."""
    conexion = get_connection()

    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("USE tienda_online")  # Seleccionar la base de datos

            # Consulta SQL para insertar productos con id_proveedor
            insertar_sql = """
                INSERT INTO productos (nombre, descripcion, precio, stock, stock_minimo, disponible, id_proveedor, activo) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """

            # Lista de productos a insertar con id_proveedor
            productos = [
                ('Laptop HP', 'Laptop HP 15" con Intel i5', 800.00, 10, 3, 1, 1, 1),
                ('Mouse Logitech', 'Mouse inalámbrico', 25.50, 50, 10, 1, 2, 1),
                ('Teclado Mecánico', 'Teclado RGB mecánico', 120.00, 20, 5, 1, 3, 1),
                ('Monitor 24"', 'Monitor Full HD', 180.00, 15, 5, 1, 4, 1),
                ('Silla Gamer', 'Silla ergonómica para oficina y gaming', 300.00, 5, 2, 1, 5, 1)
            ]

            # Ejecutar la inserción de los productos
            cursor.executemany(insertar_sql, productos)

            # Confirmar los cambios
            conexion.commit()

            print(f"✅ {cursor.rowcount} productos insertados correctamente en la tabla 'productos'.")

        except Exception as e:
            print(f"❌ Error al insertar productos: {e}")

        finally:
            cursor.close()
            conexion.close()
            print("🔌 Conexión cerrada.")

if __name__ == "__main__":
    insertar_productos()
