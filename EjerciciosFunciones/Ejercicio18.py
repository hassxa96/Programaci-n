"""
Ejercico 3: Realiza un programa en Python que calcule el máximo de una lista de números 
introducidos por el teclado. Utiliza una función que se llame máximo que no reciba nada 
como entrada y devuelva el máximo. El tamaño de la lista de números lo determina 
el usuario, al introducir un –1 se considerará que ya no quiere introducir más números.
"""


def maximo():
    lista=[]
    mayor=0
    x=int(input("Escribe un número: "))
    lista.append(x)
    while x!=-1:
        x=int(input("Escribe un número: "))
        lista.append(x)
    for i in range(len(lista)):
        if lista[i]>mayor:
            mayor=lista[i]
    return mayor


print("El mayor número de la lista es el", maximo())
