"""
Realizar un programa que conste de una clase llamada Alumno que tenga como atributos 
el nombre y la nota del alumno. Definir los métodos para inicializar sus atributos, imprimirlos y 
mostrar un mensaje con el resultado de la nota y si ha aprobado o no.
"""

class Alumno():

    def __init__(self, nombre= "",nota=0):
        self.nombre=nombre
        self.nota=nota

    def getNombre (self):
        return self.nombre
    def getNota (self):
        return self.nota

    def setNombre (self,nombre):
        self.nombre=nombre
    def setNota (self,nota):
        self.nota=nota

    def mostrar(self):
        return "Nombre: " + self.nombre + " Nota: " + str(self.nota)

    def resultado(self):
        Resultado=False
        if self.nota>=5:
            Resultado=True
        return Resultado
p1=Alumno("Jose", 7)
p2=Alumno("Adrian", 3)
print(p1.mostrar())
print(p1.resultado())
print(p2.mostrar())
print(p2.resultado())