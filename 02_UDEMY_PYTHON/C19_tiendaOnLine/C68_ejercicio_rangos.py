#Revisar si un dato está entre un rango de 5 a 5

VAL_MIN = 0
VAL_MAX = 5
dato = int(input('Ingresar un dato entero: '))


esta_dentro_rango = (VAL_MIN <= dato <= VAL_MAX)

print(f'\nLa variable está DENTRO del rango: {esta_dentro_rango} ')

# Para saber si esta FUERA del rango
esta_fuera_rango = not(VAL_MIN > dato > VAL_MAX)
print(f'\nLa variable está FUERA del rango: {esta_fuera_rango} ')