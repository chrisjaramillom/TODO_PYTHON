print('***ARGUMENTOS VARIABLES***')
# *args son argumentos y los valores se pasan en forma de tupla
# **kwargs son argumentos de key words (key, value) se pasan como diccionario

def superheroe_superpoderes(superheroe, *args, **kwargs):
    print(f'Superheroe: {superheroe} - {args} - Mas información {kwargs}')

# Llamar la función
superheroe_superpoderes('Spiderman','Instinto arganido', edad=17, empresa='Marvel')
superheroe_superpoderes('Iron Man','Armadura', 'Playboy','Millonario',  edad=37, empresa='Fox')
superheroe_superpoderes('Mi Vecino',personalidad = 'Buena Onda')