from mysql.connector import Error
import mysql.connector

def create_connection(host_name="localhost", user_name="root", user_password="", db_name="jaramillo"):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            database=db_name
        )
        print("Conexión a MySQL exitosa")
    except Error as e:
        print(f"Error: '{e}'")

    return connection

def execute_query(connection, query, params=None):
    cursor = connection.cursor()
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        connection.commit()
        print("Consulta ejecutada con éxito")
        return True
    except Error as e:
        print(f"Error: '{e}'")
        return False

def read_query(connection, query, params=None):
    cursor = connection.cursor(dictionary=True)
    result = None
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"Error: '{e}'")
        return []

if __name__ == "__main__":
    connection = create_connection()
    if connection:
        print("Conexión exitosa!")
        connection.close()