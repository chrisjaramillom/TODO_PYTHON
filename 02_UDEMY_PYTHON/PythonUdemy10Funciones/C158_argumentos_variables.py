print('***ARGUMENTOS VARIABLES***')
# *args son argumentos y los valores se pasan en forma de tupla
# **kwargs son argumentos de key words (key, value) se pasan como diccionario

def superheroe_superpoderes(superheroe, nombre, *args):
    print(f'Superheroe: {superheroe} - {nombre} - {args}')

    #Iteramos los superpoderes
    for superpoder in args:
        print(f'\tSuperpoder: {superpoder}')

# Llamar la función
superheroe_superpoderes('Spiderman','Peter Parker','Instinto arganido', 'Telaraña')
superheroe_superpoderes('Iron Man','Tony Stark','Armadura', 'Playboy','Millonario')
superheroe_superpoderes('Mi Vecino','Juan Perez')

