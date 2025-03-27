from conexion import get_connection
import hashlib

def encriptar_dato(dato):
    """Encripta un string usando SHA-256."""
    if isinstance(dato, str):
        return hashlib.sha256(dato.encode('utf-8')).hexdigest()
    return None

def encriptar_y_guardar_correos():
    conexion = get_connection()
    if not conexion:
        print("❌ No se pudo conectar a la base de datos.")
        return

    try:
        cursor = conexion.cursor()

        # Verificar si la columna 'correo_encriptado' existe
        cursor.execute("SHOW COLUMNS FROM clientes LIKE 'correo_encriptado';")
        if not cursor.fetchone():
            cursor.execute("ALTER TABLE clientes ADD COLUMN correo_encriptado VARCHAR(255);")
            print("🛠️ Columna 'correo_encriptado' añadida.")

        # Consultar correos originales
        cursor.execute("SELECT id_cliente, correo FROM clientes;")
        clientes = cursor.fetchall()

        actualizados = 0
        for id_cliente, correo in clientes:
            if correo and isinstance(correo, str):
                hash_correo = encriptar_dato(correo)
                cursor.execute(
                    "UPDATE clientes SET correo_encriptado = %s WHERE id_cliente = %s;",
                    (hash_correo, id_cliente)
                )
                actualizados += 1

        conexion.commit()
        print(f"✅ {actualizados} correos encriptados exitosamente.")

    except Exception as e:
        print(f"❌ Error: {e}")
        conexion.rollback()
    finally:
        cursor.close()
        conexion.close()

if __name__ == "__main__":
    encriptar_y_guardar_correos()
