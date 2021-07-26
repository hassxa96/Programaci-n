"""
Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. 
Construye los siguientes métodos para la clase:

Un constructor, donde los datos pueden estar vacíos.
Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
mostrar(): Muestra los datos de la persona.
esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad.
"""

class Persona():
    def __init__(self,nombre="",edad=0,DNI=""):
        self.nombre=nombre
        self.edad=edad
        self.DNI=DNI
    def getNombre(self):
        return self.nombre

    def getEdad(self):
        return self.edad

    def getDNI (self):
        return self.DNI

    def setNombre(self,nombre):
        self.nombre=nombre
    
    def setEdad(self,edad):
        self.edad=edad
    
    def setDNI(self,DNI):
        self.DNI=DNI

    def mostrar(self):
        return "nombre: " + self.nombre + " edad: " + str(self.edad) + " DNI: " + self.DNI

    def esMayorDeEdad(self):
        MayorDeEdad=False
        if self.edad>=18:
            MayorDeEdad=True
        return MayorDeEdad

p1=Persona("Luis", 20, "12345678Z")
print(p1.mostrar()) 
print(p1.esMayorDeEdad())           


