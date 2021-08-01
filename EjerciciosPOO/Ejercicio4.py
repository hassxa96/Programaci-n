"""
Desarrollar un programa que cargue los datos de un triángulo. Implementar una clase con 
los métodos para inicializar los atributos, imprimir el valor del lado 
con un tamaño mayor y  el tipo de triángulo que es (equilátero, isósceles o escaleno).
"""

class Triangulo():

    def __init__ (self):
        self.lado1=int(input("Escriba el primer lado: "))
        self.lado2=int(input("Escriba el segundo lado: "))
        self.lado3=int(input("Escriba el tercer lado: "))

    def getLado1 (self):
        return self.lado1
    def getLado2 (self):
        return self.lado2
    def getLado3 (self):
        return self.lado3

    def setLado1 (self,lado1):
        self.lado1=lado1
    def setLado2 (self,lado2):
        self.lado2=lado2
    def setLado3 (self,lado3):
        self.lado3=lado3

    def Tipo(self):
        naturaleza=0
        if self.lado1 == self.lado2 == self.lado3:
            naturaleza="El triángulo es equilátero"
        elif self.lado1 == self.lado2 != self.lado3:
            naturaleza="El triángulo es isósceles"
        else:
            naturaleza="El triángulo es escaleno"
        return naturaleza
    def LadoMayor(self):
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
           print("El lado mayor es", self.lado1)
        elif self.lado3 > self.lado2 and self.lado1 < self.lado3:
            print("El lado mayor es", self.lado3)
        else:
            print("El lado mayor es", self.lado2)       
t1=Triangulo()
print(t1.Tipo())
t1.LadoMayor()
t2=Triangulo()
print(t2.Tipo())
t2.LadoMayor()
t3=Triangulo()
print(t3.Tipo())
t3.LadoMayor()