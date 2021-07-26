"""
Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una persona) y 
cantidad (puede tener decimales). El titular será obligatorio y la cantidad es opcional. 
Construye los siguientes métodos para la clase:

Un constructor, donde los datos pueden estar vacíos.
Los setters y getters para cada uno de los atributos. El atributo no se puede modificar directamente, 
sólo ingresando o retirando dinero.
mostrar(): Muestra los datos de la cuenta.
ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, 
no se hará nada.
retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.
"""


class Cuenta():
    def __init__(self, titular="", cantidad=0):
        self.titular=titular
        self.cantidad=cantidad

    def getTitular(self):
        return self.titular
    
    def getCuenta(self):
        return self.getCuenta

    def setTitular(self,titular):
        self.titular=titular

    def setCuenta(self,cuenta):
        self.cuenta=cuenta
    
    def mostrar(self):
        return "Titular: " + self.titular + " Cuenta " + str(self.cantidad)
    
    def ingresar(self,cantidad):
        if cantidad>=0:
            self.cantidad=self.cantidad+cantidad
        return self.cantidad

    def retirar(self,cantidad):
        if cantidad>=0:
            self.cantidad=self.cantidad-cantidad
        return self.cantidad

p1=Cuenta("Antonio", 100)
print(p1.ingresar(30))
print(p1.retirar(50))
print(p1.mostrar())

    
