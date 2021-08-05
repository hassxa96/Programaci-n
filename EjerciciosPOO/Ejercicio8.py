"""
Desarrollar un programa que conste de una clase padre Cuenta y dos subclases PlazoFijo y CajaAhorro. 
Definir los atributos titular y cantidad y un método para imprimir los datos en la clase Cuenta. 
La clase CajaAhorro tendrá un método para heredar los datos y uno para mostrar la información.

La clase PlazoFijo tendrá dos atributos propios, plazo e interés. Tendrá un método para obtener el 
importe del interés (cantidad*interés/100) y otro método para mostrar la información, datos del 
titular plazo, interés y total de interés.

Crear al menos un objeto de cada subclase.
"""

class Cuenta():
    def __init__ (self, titular, cantidad):
        self.titular= titular
        self.cantidad=cantidad

    def getTitular(self):
        return self.titular
    def getCantidad (self):
        return self.cantidad

    def setTitular (self,titular):
        self.titular=titular
    def setCantidad (self,cantidad):
        self.cantidad=cantidad

    def mostrar_datos(self):
        return "Titular: " + self.titular + " Cantidad: " + str(self.cantidad)


class CajaAhorro(Cuenta):
    def __init__(self, titular, cantidad):
        super().__init__(titular,cantidad)
    
    def imprimir(self):
        super().mostrar_datos()

class PlazoFijo(Cuenta):
    def __init__(self,titular,cantidad,plazo,interes):
        super().__init__(titular,cantidad)
        self.plazo=plazo
        self.interes=interes
    
    def importe_interes(self):
        total= self.cantidad*self.interes/100
        print("El importe del interés es: ", total)

    def imprimir(self):
        super().mostrar_datos()
        self.importe_interes()
    
c1=CajaAhorro("Raul",1000)
c1.imprimir()
p1=PlazoFijo("Manuel", 200, 3, 10)
p1.imprimir()