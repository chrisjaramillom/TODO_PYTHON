print('***Función range***')

print('Secuencia del 0 al 4:')
# inicio = 0 (opcional)
# fin = 5 -1 = 4
# incremento = 1 (opcional)

mensaje = input('Ingrese el mensaje a repetir: ')
num_rep = int(input('Ingrese cantidad de veces a repetir: '))

for i in range(num_rep):
    print(f'{i+1}.- {mensaje}')