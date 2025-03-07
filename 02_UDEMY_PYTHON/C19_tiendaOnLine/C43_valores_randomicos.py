# Valores aleatorios o randómicos con la función randint

#import random --es una forma de importar la librería random
# para utilizar el import random se hace:
# import random
# numero = random.randint(1,10)

from random import randint

# Generar valor aleatorio entre 1 y 10
numero = randint(1,10)
print(f'Número aleatorio entre 1 y 10: {numero}')

# Simulación de un dado de 6 caras
dado = randint(1,6)
print(f'\nResultado de lanzar el dado: {dado}')
