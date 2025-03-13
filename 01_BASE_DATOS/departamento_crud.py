from database import create_connection, execute_query, read_query

def crear_departamento(nombre, ubicacion, bandera):
    """
    Crea un nuevo departamento en la base de datos
    """
    connection = create_connection()
    query = """
    INSERT INTO departamento (DEP_NOMBRE, DEP_UBICA, DEP_BANDERA) 
    VALUES (%s, %s, %s)
    """
    params = (nombre, ubicacion, bandera)
    
    success = execute_query(connection, query, params)
    connection.close()
    return success

def obtener_departamentos():
    """
    Obtiene todos los departamentos de la base de datos
    """
    connection = create_connection()
    query = "SELECT * FROM departamento"
    
    departamentos = read_query(connection, query)
    connection.close()
    return departamentos

def obtener_departamento_por_id(id):
    """
    Obtiene un departamento específico por su ID
    """
    connection = create_connection()
    query = "SELECT * FROM departamento WHERE DEP_ID = %s"
    
    departamentos = read_query(connection, query, (id,))
    connection.close()
    
    if departamentos:
        return departamentos[0]
    return None

def actualizar_departamento(id, nombre, ubicacion, bandera):
    """
    Actualiza un departamento existente
    """
    connection = create_connection()
    query = """
    UPDATE departamento 
    SET DEP_NOMBRE = %s, DEP_UBICA = %s, DEP_BANDERA = %s 
    WHERE DEP_ID = %s
    """
    params = (nombre, ubicacion, bandera, id)
    
    success = execute_query(connection, query, params)
    connection.close()
    return success

def eliminar_departamento(id):
    """
    Elimina un departamento de la base de datos
    """
    connection = create_connection()
    query = "DELETE FROM departamento WHERE DEP_ID = %s"
    
    success = execute_query(connection, query, (id,))
    connection.close()
    return success