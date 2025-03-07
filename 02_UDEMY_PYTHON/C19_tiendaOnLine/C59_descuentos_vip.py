# Sistema de Descuentos VIP

print('***SISTEMA DE DESCUENTOS VIP***')

NO_PRODUCTOS_DESCUENTO=10
cantidad_productos = int(input('Cuantos productos has comprado hoy? '))
tienda_membresia = input('Tienes la membresía de la tienda (Si / No)?')

es_elegible_descuento = (cantidad_productos >= NO_PRODUCTOS_DESCUENTO
                         and tienda_membresia.strip().lower() == 'si')

print(f'\nTienes acceso al descuento VIP: {es_elegible_descuento} ')