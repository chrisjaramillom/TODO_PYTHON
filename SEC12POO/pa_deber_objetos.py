#Deber de Objetos y Herencia en Python

class Animal:
    def __init__(self, nombre=None):
        self.nombre = nombre
                    
    def hacer_sonido(self):
        print ("El animal hace un sonido")

class Perro(Animal):
    #Sobreescritura (POLIMORFISMO) del método hacer_sonido del padre
    def hacer_sonido(self):
        print ("El perro ladra: Guau, guau!!!")
    

# Programa Principal

#Definir un objeto de la clase Animal (padre)
print ("Objeto de la clase padre")
animal1  = Animal('Papito')
animal1.hacer_sonido();

#Definir un objeto de la clase Perro (hija)

print ("\nObjeto de la clase hija")
perro1 = Perro('Istercito')
perro1.hacer_sonido();  #Ejemplo de polimorfismo
