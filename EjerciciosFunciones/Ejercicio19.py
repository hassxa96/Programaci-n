#Ejercicio 4: Función para determinar si dos listas son iguales.

def iguales(a,b):
    contador=0
    for i,h in zip(a,b):
        if i!=h:
            contador+=1
    if contador!=0:
        contador="Las listas son distintas"
    else:
        contador="Las listas son iguales"
    return contador
lista1=[]
lista2=[]
x=int(input("Escribe un número: "))
lista1.append(x)
while x!=0:
    x=int(input("Escribe un número: "))
    lista1.append(x)
print("La primera lista es", lista1)

y=int(input("Introduce un número: "))
lista2.append(y)
while y!=0:
    y=int(input("Introduce un número: "))
    lista2.append(y)
print("La segunda lista es", lista2)

print(iguales(lista1,lista2))