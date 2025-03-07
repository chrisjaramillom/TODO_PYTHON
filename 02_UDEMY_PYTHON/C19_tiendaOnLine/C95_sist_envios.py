print('***SISTEMA DE ENVÍOS***')

TNACIONA = 10
TINTERNACIONAL = 20
destino = input('Ingrese el destino del paquete (Ecuador, Colombia, etc: ').strip().lower()
peso = float(input('Ingrese el peso del paquete (Kg: '))

destino_nacional = destino == 'ecuador'


if destino_nacional:
    valor_envio = peso * TNACIONA
else:
    valor_envio = peso * TINTERNACIONAL

if valor_envio is not None:
    print('\n****SERVICIO DE ENVIOS****')
    print(f'El país del envío es: {destino}')
    print(f'El peso del paquete es: {peso:.2f}')
    print(f'El valor a cancelar por el envío es: $ {valor_envio:.2f} USD')
else:
    print('No se ha podido calcular valores!!!')
