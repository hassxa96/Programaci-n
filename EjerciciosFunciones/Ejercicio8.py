"""
Solicitar números al usuario hasta que ingrese el cero. Por cada uno, mostrar la suma de sus dígitos 
(utilizando una función que realice dicha suma).
"""

def suma_digitos(x):
    contador=0
    while x!=0:
        y=x%10 #y=5
        contador+=y #contador=11
        x=x//10 #x=0
    return contador
suma=0
y=int(input("Escribe un número: ")) #y=40
while y!=0:
    print(suma_digitos(y)) #4
    suma+=y
    y=int(input("Escribe un número: ")) #y=13
print("La suma de los dígitos es", suma)