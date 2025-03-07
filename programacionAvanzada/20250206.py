
nombre = "Luis"
print(nombre)

nombre2 = 'Chris'
print(nombre2)

apellido = "Jaramillo"

#Concatenación
nom_completo = nombre + ' ' + apellido
print( nom_completo)
print(f'{nombre2} {apellido}')

# Repetición
saludo = 'Hola' * 3
print(saludo)

# Indexación y Slicing (corte de string)
nombre = 'Alejo'
print(nombre[0])


nombre3 = 'Montufar'
print(nombre3[2:5])

#Funciones propias de String
cadena = 'Hola, mundo'
print(cadena)

# Obtener la longitud de un string
print(len(cadena))

# Cambiar mayúsculas a minúsculas y viceversa
print(cadena.lower())
print(cadena.upper())
print(cadena.capitalize())
print(cadena.strip())  #eliminar espacios al inicio y final

# Reemplazar pedazo de cadena
cadena2 = cadena.replace('mundo', 'AMIGO')
print(cadena2)

# Dividir un string en una lista
cadena3 = cadena.split(", ")
print(cadena3)

texto = 'Contrary to popular belief, Lorem Ipsum is not simply random text. It has roots in a piece of classical Latin literature from 45 BC, making it over 2000 years old. Richard McClintock, a Latin professor at Hampden-Sydney College in Virginia, looked up one of the more obscure Latin words, consectetur, from a Lorem Ipsum passage, and going through the cites of the word in classical literature, discovered the undoubtable source. Lorem Ipsum comes from sections 1.10.32 and 1.10.33 of "de Finibus Bonorum et Malorum" (The Extremes of Good and Evil) by Cicero, written in 45 BC. This book is a treatise on the theory of ethics, very popular during the Renaissance. The first line of Lorem Ipsum, Lorem ipsum dolor sit amet.., comes from a line in section 1.10.32.'
print(texto)

lista_texto = texto.split()
print(len(lista_texto))

#Busca el índice de la primera aparición de un substring
print(texto.find("random"))

#Contar palabras
print(texto.count("Lorem"))

#Ejemplo verificar los indices donde aparece lorem
palabra = 'Lorem'
indices = []
indice = texto.find(palabra)

while indice != -1:
    indices.append(indice)
    indice = texto.find(palabra, indice + 1)

print(indices)


#CLASE 2025 02 13

# Cuadrado de un número usando lambda
# La función de lambda va a recibir un número como argumento y va a devolver el cuadrado de dicho número
cuadrado = lambda numero: numero ** 2
print(cuadrado(5))  # Ejemplo de uso


