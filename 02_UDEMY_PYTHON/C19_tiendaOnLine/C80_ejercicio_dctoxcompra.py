print('***DESCUENTOS EN LOCAL***')


monto = int(input('Cuál fue el monto de tu compra: '))
miembro = input('Eres miembro de la tienda: (si/no): ')


if (miembro.strip().lower() == 'si') and (monto > 1500):
    dcto = 0.1
    mon_dcto = monto * dcto
    print(f'Felicidades, has obtenido un descuento del {dcto * 100}%')
    print(f'Monto de la compra {monto}')
    print(f'Monto del descuento {mon_dcto}')
    print(f'Monto final de la compra con descuento {monto - mon_dcto}')
elif (miembro.strip().lower() == 'si') and (monto < 1500):
    dcto = 0.05
    mon_dcto = monto * dcto
    print(f'Felicidades, has obtenido un descuento del {dcto * 100}%')
    print(f'Monto de la compra {monto}')
    print(f'Monto del descuento {mon_dcto}')
    print(f'Monto final de la compra con descuento {monto - mon_dcto}')
elif (miembro.strip().lower() == 'no') and (monto > 1500):
    dcto = 0.03
    mon_dcto = monto * dcto
    print(f'Felicidades, has obtenido un descuento del {dcto * 100}%')
    print(f'Monto de la compra {monto}')
    print(f'Monto del descuento {mon_dcto}')
    print(f'Monto final de la compra con descuento {monto - mon_dcto}')
    print('Si te afilias podrás obtener un descuento mayor')
else:
    print(f'No obtuviste ningún tipo de descuento')
    print(f'Te invitamos a hacerte miembro de la tienda')
    print(f'Monto de la compra {monto}')

