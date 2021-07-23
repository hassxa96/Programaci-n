"""
Ejercicio 1 Tarea : Escribir un programa que pida números al usuario, mostrar el factorial de cada uno y, 
al finalizar, 
la cantidad total de números leídos en total. Utilizar una o más funciones, según sea necesario.
"""

def factorial(x):
    contador=1
    for i in range(1, x+1):
      contador*=i
    return contador
    
total=0
y=int(input("Escribe un número: "))
while y>=0:
    total+=1
    print("El factorial de", y, "es", factorial(y))
    y=int(input("Escribe un número: "))

print("El total de números introducidos válidos para calcular su factorial es", total)