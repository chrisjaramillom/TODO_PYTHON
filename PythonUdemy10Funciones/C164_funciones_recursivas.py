print('FUNCIONES RECURSIVAS')

#DEFINIR UNA FUNCION LLAMADA recursiva
def funcion_recursiva(numero):
    #Caso Base
    if numero==1:
        print(numero, end=' ') #1
    else: # Caso recursivo
        funcion_recursiva((numero -1))
        print(numero, end=' ')

#Programa Principal
funcion_recursiva()