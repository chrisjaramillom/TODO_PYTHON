def generar_correo(nombre_completo, empresa, extension=".gob.ec"):
    """
    Genera un correo electrónico basado en el nombre del colaborador,
    la empresa y la extensión del dominio.

    :param nombre_completo: Nombre completo del colaborador.
    :param empresa: Nombre de la empresa.
    :param extension: Extensión del dominio (por defecto, ".gob.ec").
    :return: Correo electrónico generado.
    """
    # Normalizar el nombre
    nombre_normalizado = nombre_completo.strip().lower().replace(' ', '.')

    # Normalizar el dominio
    dominio = empresa.strip().lower() + extension

    # Generar el correo
    correo = f"{nombre_normalizado}@{dominio}"

    # Resultados
    return nombre_completo, nombre_normalizado, empresa, dominio, correo


# Entrada de datos
nombre = 'Christian Alejandro Jaramillo Montufar'
empresa = 'GADMUR'

# Llamada a la función
nombre_original, nombre_normalizado, empresa_original, dominio, correo = generar_correo(nombre, empresa)

# Mostrar los resultados
print('***Generador de Correos***')
print(f'Nombre del Colaborador: {nombre_original}')
print(f'Nombre Normalizado: {nombre_normalizado}')

print()
print('***Datos***')
print(f'Nombre de la Empresa: {empresa_original}')
print(f'Nombre Dominio: {dominio}')

print()
print('***Correo Electrónico***')
print(f'Correo del Colaborador: {correo}')
