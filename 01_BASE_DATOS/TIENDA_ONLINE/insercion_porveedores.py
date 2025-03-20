from conexion import get_connection

def insertar_proveedores():
    """Inserta proveedores en la tabla 'proveedores' de la base de datos 'tienda_online'."""
    conexion = get_connection()

    if conexion:
        try:
            cursor = conexion.cursor()
            cursor.execute("USE tienda_online")  # Seleccionar la base de datos

            # Consulta SQL para insertar proveedores
            insertar_sql = """
                INSERT INTO proveedores (nombre, contacto, telefono, direccion, activo) 
                VALUES (%s, %s, %s, %s, %s)
            """

            # Lista de proveedores a insertar
            proveedores = [
                ('Distribuidora Tecno', 'José Ramírez', '0981112223', 'Av. Industrial 999', 1),
                ('ElectroHogar', 'Luis Salinas', '0993322110', 'Calle Comercio 555', 1),
                ('MegaTech', 'Andrés Villalba', '0974433221', 'Plaza Central 777', 1),
                ('Gamer World', 'Carla Mendoza', '0965544332', 'Zona Comercial 888', 1),
                ('Office Solutions', 'Ricardo Pérez', '0956677889', 'Parque Empresarial 666', 1)
            ]

            # Ejecutar la inserción de los proveedores
            cursor.executemany(insertar_sql, proveedores)

            # Confirmar los cambios
            conexion.commit()

            print(f"✅ {cursor.rowcount} proveedores insertados correctamente en la tabla 'proveedores'.")

        except Exception as e:
            print(f"❌ Error al insertar proveedores: {e}")

        finally:
            cursor.close()
            conexion.close()
            print("🔌 Conexión cerrada.")

if __name__ == "__main__":
    insertar_proveedores()

