"""
•	Crea al menos un objeto de cada subclase y añádelos a una lista llamada vehiculos.
•	Realiza una función llamada catalogar() que reciba la lista de vehiculos y 
los recorra mostrando el nombre de su clase y sus atributos.
•	Modifica la función catalogar() para que reciba un argumento optativo ruedas, 
haciendo que muestre únicamente los que su número de ruedas concuerde con el valor del argumento. 
También debe mostrar un mensaje "Se han encontrado {} vehículos con {} ruedas:" 
únicamente si se envía el argumento ruedas. Ponla a prueba con 0, 2 y 4 ruedas como valor.
"""

class Vehiculo():
    def __init__(self,color,ruedas):
        self.color=color
        self.ruedas=ruedas
    
    def getColor (self):
        return self.color
    def getRuedas (self):
        return self.ruedas

    def setColor(self,color):
        self.color=color
    def setRuedas(self,ruedas):
        self.ruedas=ruedas

    def catalogar(self):
        return "Color: " + self.color + " .Ruedas: " + str(self.ruedas)
    
class Coche(Vehiculo):
    def __init__(self,color,ruedas,velocidad,cilindrada):
        super().__init__(color,ruedas)
        self.velocidad=velocidad
        self.cilindrada=cilindrada
    
    def catalogar(self):
        return super().catalogar() + " .Velocidad: " + str(self.velocidad) + " .Cilindrada: " + str(self.cilindrada)
        
class Camioneta (Coche):
    def __init__(self,color,ruedas,velocidad,cilindrada,carga):
        super().__init__(color,ruedas,velocidad,cilindrada)
        self.carga=carga
    
    def catalogar(self):
        return super().catalogar() + " .Carga: " + str(self.carga)

class Bicicleta(Vehiculo):
    def __init__(self,color,ruedas,tipo):
        super().__init__(color,ruedas)
        self.tipo=tipo

    def catalogar(self):
        return super().catalogar() + " .Tipo: " + self.tipo

class Motocicleta(Bicicleta):
    def __init__(self,color,ruedas,tipo,velocidad,cilindrada):
        super().__init__(color,ruedas,tipo)
        self.velocidad=velocidad
        self.cilindrada=cilindrada

    def catalogar(self):
        return super().catalogar() + " .Velocidad: " + str(self.velocidad) + " .Cilindrada: " + str(self.cilindrada)

"""
Realiza una función llamada catalogar() que reciba la lista de vehiculos y 
los recorra mostrando el nombre de su clase y sus atributos.
•	Modifica la función catalogar() para que reciba un argumento optativo ruedas, 
haciendo que muestre únicamente los que su número de ruedas concuerde con el valor del argumento. 
También debe mostrar un mensaje "Se han encontrado {} vehículos con {} ruedas:" 
únicamente si se envía el argumento ruedas. Ponla a prueba con 0, 2 y 4 ruedas como valor.
"""
def catalogar(lista,ruedas):
    contador=0
    if ruedas!=0:
        for i in lista:
            if ruedas == i.ruedas:
                contador+=1
        print("Se han encontrado",contador,"vehículos con", ruedas, "ruedas")
        for i in lista:
            print(type(i).__name__, i.catalogar())
    
lista=[
    Coche("Rojo", 4 , 220 , 120),
    Camioneta("Gris", 4 , 180 , 140 , 400),
    Bicicleta("Azul", 2 , "Urbana"),
    Motocicleta("Verde", 2 , "Urbana", 200 , 110)
]
catalogar(lista,2)
print()
catalogar(lista,4)