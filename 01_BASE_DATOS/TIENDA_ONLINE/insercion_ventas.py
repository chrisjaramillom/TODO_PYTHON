from conexion import get_connection

def insertar_pedidos_detalles_pagos():
    """Inserta registros en las tablas 'pedidos', 'detalle_pedido' y 'pagos' de la base de datos 'tienda_online'."""
    conexion = get_connection()

    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("USE tienda_online")  # Seleccionar la base de datos

            # Insertar pedidos
            pedidos_sql = """
                INSERT INTO pedidos (id_cliente, total, estado, activo) 
                VALUES (%s, %s, %s, %s)
            """
            pedidos = [
                (1, 850.00, 'pendiente', 1),
                (2, 45.00, 'enviado', 1),
                (3, 200.00, 'entregado', 1),
                (4, 320.00, 'pendiente', 1),
                (5, 500.00, 'cancelado', 1)
            ]
            cursor.executemany(pedidos_sql, pedidos)
            conexion.commit()
            print(f"✅ {cursor.rowcount} pedidos insertados correctamente.")

            # Obtener los IDs de los pedidos insertados
            cursor.execute("SELECT id_pedido FROM pedidos ORDER BY id_pedido DESC LIMIT 5")
            pedidos_ids = [row[0] for row in cursor.fetchall()]

            # Obtener los IDs de los productos existentes
            cursor.execute("SELECT id_producto FROM productos ORDER BY id_producto ASC LIMIT 5")
            productos_ids = [row[0] for row in cursor.fetchall()]

            if len(productos_ids) < 5:
                raise Exception("No hay suficientes productos en la base de datos para asociar a los pedidos.")

            # Insertar detalles de pedidos con IDs de productos existentes
            detalles_sql = """
                INSERT INTO detalle_pedido (id_pedido, id_producto, cantidad, precio_unitario, subtotal, activo) 
                VALUES (%s, %s, %s, %s, %s, %s)
            """
            detalles = [
                (pedidos_ids[0], productos_ids[0], 1, 800.00, 800.00, 1),
                (pedidos_ids[1], productos_ids[1], 2, 25.50, 51.00, 1),
                (pedidos_ids[2], productos_ids[2], 1, 120.00, 120.00, 1),
                (pedidos_ids[3], productos_ids[3], 2, 180.00, 360.00, 1),
                (pedidos_ids[4], productos_ids[4], 1, 300.00, 300.00, 1)
            ]
            cursor.executemany(detalles_sql, detalles)
            conexion.commit()
            print(f"✅ {cursor.rowcount} detalles de pedidos insertados correctamente.")

            # Insertar pagos
            pagos_sql = """
                INSERT INTO pagos (id_pedido, metodo_pago, monto, activo) 
                VALUES (%s, %s, %s, %s)
            """
            pagos = [
                (pedidos_ids[0], 'tarjeta', 850.00, 1),
                (pedidos_ids[1], 'efectivo', 45.00, 1),
                (pedidos_ids[2], 'transferencia', 200.00, 1),
                (pedidos_ids[3], 'tarjeta', 320.00, 1),
                (pedidos_ids[4], 'efectivo', 500.00, 1)
            ]
            cursor.executemany(pagos_sql, pagos)
            conexion.commit()
            print(f"✅ {cursor.rowcount} pagos insertados correctamente.")

        except Exception as e:
            print(f"❌ Error al insertar datos: {e}")

        finally:
            cursor.close()
            conexion.close()
            print("🔌 Conexión cerrada.")

if __name__ == "__main__":
    insertar_pedidos_detalles_pagos()
