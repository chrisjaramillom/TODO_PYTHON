print('***DETALLES PERSONA CON KWARGS***')

#Función que acepta argumentos variables en forma de llave - valor (diccionario)

def imprimir_detalle_persona(**kwargs):
    print(f'\nValores recibidos:')
    for llave, valor in kwargs.items():
        print(f'{llave}: {valor}')


# Llamar a la función
imprimir_detalle_persona(nombre='Karla', edad=30, ciudad='México')
imprimir_detalle_persona(nombre='Mario', apellido='Juarez', edad=33, ciudad='Ecuador')
imprimir_detalle_persona() # Imprime solo el mensaje pero el diccionario está vacío
