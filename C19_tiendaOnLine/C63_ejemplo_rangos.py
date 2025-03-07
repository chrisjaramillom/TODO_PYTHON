#Revisar si un dato está entre un rango de 1 a 10

dato = int(input('Ingresar un dato entero: '))


esta_dentro_rango = 1 <= dato <= 10

print(f'\nLa variable está DENTRO del rango: {esta_dentro_rango} ')

# Para saber si esta FUERA del rango
esta_fuera_rango = not(1 <= dato <= 10)

print(f'\nLa variable está FUERA del rango: {esta_fuera_rango} ')
