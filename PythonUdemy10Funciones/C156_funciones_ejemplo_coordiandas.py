print('Obtener Coordenadas X Y y Z')

def obtener_coordenadas():
    x, y, z = 10, 20, 30
    return (x, y, z)

#Llamar la función
resultado_coordenadas = obtener_coordenadas()
print(resultado_coordenadas)

#Unpacking de la tupla
x1, y1, z1 = resultado_coordenadas

print(f'Coordnadas x = {x1}, y = {y1}, z = {z1}')