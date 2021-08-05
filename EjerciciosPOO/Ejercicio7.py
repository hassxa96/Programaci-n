"""
En un banco tienen clientes que pueden hacer depósitos y extracciones de dinero. 
El banco requiere también al final del día calcular la cantidad de dinero que se ha depositado.
Se deberán crear dos clases, la clase cliente y la clase banco. La clase cliente tendrá los atributos 
nombre y cantidad y los métodos _init_, depositar, extraer, mostrar_total.
La clase banco tendrá como atributos 3 objetos de la clase cliente y los métodos _init_, operar y 
deposito_total.
"""

class Cliente():

    def __init__ (self, nombre=" ", cantidad=" "):
        self.nombre=nombre
        self.cantidad=cantidad

    def getNombre (self):
        return self.nombre
    def getCantidad (self):
        return self.cantidad

    def setNombre (self, nombre):
        self.nombre=nombre
    def setCantidad (self, cantidad):
        self.cantidad=cantidad

    def depositar (self, cantidad):
        if cantidad>=0:
            self.cantidad= self.cantidad + cantidad
        return self.cantidad
    def extraer (self,cantidad):
        if cantidad>=0:
            self.cantidad=self.cantidad-cantidad
        return self.cantidad
    def mostrar_total(self):
        return "Nombre: " + self.nombre + " Cantidad: " + str(self.cantidad)

class Banco ():
    def __init__ (self):
        self.c1=Cliente("Alberto.",300)
        self.c2=Cliente("Antonio.", 500)
        self.c3=Cliente("Claudio.", 700)

    def operar (self):
        self.c1.depositar(200)
        self.c2.depositar(80)
        self.c3.extraer(100)

    def mostrar_total(self):
        Total= self.c1.cantidad + self.c2.cantidad + self.c3.cantidad
        print("El total del dinero del banco es: ", Total)

b1=Banco()
b1.operar()
b1.mostrar_total()