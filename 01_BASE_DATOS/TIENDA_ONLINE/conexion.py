import mysql.connector
from mysql.connector import Error

def get_connection():
    try:
        conexion = mysql.connector.connect(
            host="localhost",        # Cambia por tu host si es diferente
            user="root",       # Reemplaza con tu usuario de MySQL
            password="", # Reemplaza con tu contraseña de MySQL
            database="tienda_online"
        )

        if conexion.is_connected():
            print("✅ Conexión exitosa a MySQL")
            return conexion

    except Error as e:
        print(f"❌ Error al conectar a MySQL: {e}")
        return None

# Prueba de conexión
if __name__ == "__main__":
    conexion = get_connection()
    if conexion:
        conexion.close()
        print("🔌 Conexión cerrada.")
