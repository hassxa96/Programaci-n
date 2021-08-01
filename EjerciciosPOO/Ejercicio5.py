"""
Realizar un programa en el cual se declaren dos valores enteros por teclado utilizando el método _init_. 
Calcular después la suma, resta, multiplicación y división. 
Utilizar un método para cada una e imprimir los resultados obtenidos. Llamar a la clase Calculadora.
"""

class Calculadora():

    def __init__ (self):
        self.valor1=int(input("Escribe el primer valor: "))
        self.valor2=int(input("Escribe el segundo valor: "))

    def getValor1 (self):
        return self.valor1
    def getValor2 (self):
        return self.valor2

    def setValor1 (self, valor1):
        self.valor1=valor1
    def setValor2 (self, valor2):
        self.valor2=valor2

    def Suma(self):
        return self.valor1 + self.valor2
    def Resta(self):
        return self.valor1 - self.valor2
    def Multiplicacion(self):
        return self.valor1 * self.valor2
    def Division(self):
        return self.valor1 / self.valor2

p1=(Calculadora())
print("La suma es: ", p1.Suma())
print("La resta es: ", p1.Resta())
print("La multiplicación es: ", p1.Multiplicacion())
print("La división es: ", p1.Division())