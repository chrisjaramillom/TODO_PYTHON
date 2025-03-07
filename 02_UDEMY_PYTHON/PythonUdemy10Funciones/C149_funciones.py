# Ejemplo de funciones
# Una función debe ser definida para poder ser llamada
# es por esto que las funciones deben estar antes del programa

print('***FUNCIONES EN PYTHON***')

# Definir una función para mandar a saludar
def saludar(mensaje:str): # Definición o cabecera de una función
    #Cuerpo de la función
    print(f'Saludos de adentro de la función {mensaje}!!!')

# Programa Principal
saludar('Hijo')
saludar('de')
saludar('Cuca')