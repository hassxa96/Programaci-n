"""
Requerir al usuario que 
ingrese un número entero e informar si es primo o no, utilizando una función booleana que lo decida
"""

def funcion():
    contador=0
    Primo=False
    x=int(input("Escribe un número primo: "))
    for i in range(1,x+1):
        if x%i==0:
            contador+=1
    if contador==2:
        Primo=True

    return Primo
print(funcion())