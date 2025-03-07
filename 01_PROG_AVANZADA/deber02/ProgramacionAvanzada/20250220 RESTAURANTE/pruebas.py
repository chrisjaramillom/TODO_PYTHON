import mysql.connector

try:
    # Conexión a la base de datos
    conexion = mysql.connector.connect(
        host='localhost',  # Asegúrate de que tu servidor está en localhost
        user='root',
        password='',  # Deja la contraseña vacía si MySQL lo permite
        database='jardineria'
    )

    cursor = conexion.cursor()

    # Consulta SQL
    consulta = "SELECT * FROM cliente"
    cursor.execute(consulta)

    # Obtener los nombres de las columnas
    columnas = [desc[0] for desc in cursor.description]
    print(" | ".join(columnas))  # Imprimir encabezado de la tabla
    print("-" * 50)

    # Imprimir cada fila de resultados
    for fila in cursor.fetchall():
        print(" | ".join(map(str, fila)))

except mysql.connector.Error as error:
    print(f"Error al conectar con MySQL: {error}")

finally:
    # Cerrar conexión
    if 'cursor' in locals():
        cursor.close()
    if 'conexion' in locals():
        conexion.close()

