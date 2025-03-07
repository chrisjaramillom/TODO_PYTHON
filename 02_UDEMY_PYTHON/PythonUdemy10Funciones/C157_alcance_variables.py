print('***ALCANCE DE VARIABLES***')

#Definición de variables locales y globales dentro del programa
#Declaramos una variable global
contador_global = 0

def incrementar_contador():
    #Declaramos una variable local
    contador_local= 0
    #declaramos la var global dentro de la función para poder utilizarla
    global contador_global
    # Incrementamos la variable global
    contador_global += 1
    # Incrementamos la variable local
    contador_local += 1
    #Imprimimos ambos contadores
    print(f'Contador Local : {contador_local}')
    print(f'Contador Global : {contador_global}')

incrementar_contador()
incrementar_contador()
incrementar_contador()
incrementar_contador()

# Como se puede ver en el resultado el contador local siempre se encera y empieza en 1
# mientras que el contador global va aumentando según las veces que se llame a la función

