"""
21.
Introducir dos números enteros por teclado. El programa debe:
• Imprimir los números que hay entre ellos, empezando por el más pequeño, independientemente del
orden introducido.
• Calcular y visualizar cuantos números hay, cuántos de ellos son pares y su suma.
Ejecución:
Primer número: 2
Segundo numero: 9
3
4
5
6
7
8
9
Entre 2 y 9 hay 7 números siendo 4 pares
La suma de los pares es 20
"""
x=int(input("Escribe el primer número: "))
y=int(input("Escribe el segundo número: "))
contador=0
suma=0
for i in range(x,y+1):
    print(i)
    if i%2==0:
        contador+=1
        suma+=i
print("Entre", x, "y", y, "hay", y-x, "numero siendo", contador, "pares")
print("La suma de los pares es", suma)