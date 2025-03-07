#Ejemplo de Objetos y Herencia y Polimorfismo en Python

class Animal:
    def __init__(self, nombre=None):
        self.nombre = nombre
                
    def comer(self):
        print ("puedo comer mucho")

    def dormir(self):
        print ("duermo varias horas")
    
    def hacer_sonido(self):
        print ("me comunico mediante sonidos")

class Perro(Animal):
    def jugar(self):
        print ("me gusta jugar")
    
    #Sobreescritura del método dormir del padre
    def dormir(self):
        print ("duermo al rededor de 15 horas")
    
    #Sobreescritura (POLIMORFISMO) del método hacer_sonido del padre
    def hacer_sonido(self):
        print ("Yo ladro para comunicarme")
    

class Gato(Animal):
    def cazar(self):
        print ("yo cazo ratones")
    
    #Sobreescritura del método dormir del padre
    def dormir(self):
        print ("duermo al rededor de 10 horas")
    
    #Sobreescritura (POLIMORFISMO) del método hacer_sonido del padre
    def hacer_sonido(self): # Ejemplo de polimorfismo
        print ("Yo maullo para comunicarme")

#Función Polimorfica, duck typing
def hacer_sonido_animal(animal):
    animal.hacer_sonido()
 
# Programa Principal

#Definir un objeto de la clase padre
print ("Ejemplo de Herencia en Python")
print ("Objeto de la clase padre")
animal1  = Animal()
animal1.comer();
animal1.dormir();
animal1.hacer_sonido();
print ("\nLlamada a la funcion duck typing")
hacer_sonido_animal(animal1)

print ("************************************")
#Definir un objeto de la clase hija
print ("\nObjeto de la clase hija")
perro1 = Perro()
perro1.comer();
perro1.dormir();
perro1.jugar();
perro1.hacer_sonido();  #Ejemplo de polimorfismo
print ("\nLlamada a la funcion duck typing")
hacer_sonido_animal(perro1)

print ("************************************")
#Definir un objeto de la clase hija
print ("\nObjeto de la clase hija")
gato1 = Gato()  
gato1.comer();
gato1.dormir();
gato1.cazar();  
gato1.hacer_sonido(); #Ejemplo de polimorfismo
print ("\nLlamada a la funcion duck typing")
hacer_sonido_animal(gato1)

