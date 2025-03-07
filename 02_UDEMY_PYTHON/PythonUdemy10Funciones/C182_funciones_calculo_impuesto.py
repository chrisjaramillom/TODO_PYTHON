print('*** Sistema IMPUESTOS con Funciones ***')

def datos():
    monto = float(input('Ingresa el monto de ingreso:'))
    impuesto = float(input('Ingrese el porcentaje (%):'))
    pago_total = monto + (monto * impuesto / 100)
    return(pago_total)

# Programa principal
if __name__ == '__main__':
    # Creamos el menu
    while True:
        total = datos()
        print(f'El total a pagar es: {total}')
        repetir = input('Desea realizar otro cálculo? : S o N')
        if repetir == 'N' or repetir == 'n':
            break