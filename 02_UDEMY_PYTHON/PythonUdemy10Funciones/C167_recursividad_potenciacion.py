print('***POTENCIACIÓN DEL NUMERO***')

#Definir la función potenciación recursiva
def potenciacion_recursiva(base, exponente):
    #Caso Base
    potenciacion = 1
    if exponente==0 and not base == 0:
        print(f' Todo número elevado a {exponente} es: 1') #1
        return 1
    else: # Caso recursivo
        potenciacion = base * potenciacion_recursiva(base, exponente - 1)
        print(f'Potencia de {base} elevado a {exponente} es: {potenciacion}')
        return potenciacion

#Programa Principal

base = 0
exponente = 0
base = int(input('Ingrese el valor de la base:  '))
exponente = int(input('Ingrese el valor del exponente:  '))
resultado = potenciacion_recursiva(base, exponente)
print(f'La potencia de {base} elevado a {exponente} es {resultado} ')