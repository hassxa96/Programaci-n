"""
Ejercicio 2: Un número perfecto es aquel que es igual a la suma de todos sus divisores excepto él mismo.
El primer número perfecto es 6, ya que 1+2+3=6. Escribir un programa 
que muestre todos los números perfectos hasta un número dado leído del teclado
"""

def divisores(x):
    lista=[]
    for i in range(1,x):
        if x%i==0:
            lista.append(i)
    return lista

def suma_lista(x):
    suma=0
    for i in x:
        suma=suma+i
    return suma

lista=[]
suma=0
y=int(input("Escribe un número: "))
for i in range(1,y+1):
    lista=divisores(i)
    suma=suma_lista(lista)
    if suma==i:
        print(i)
