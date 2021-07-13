"""
10.Escriba un programa que permita crear una lista de palabras y que, a continuación, pida dos palabras y 
sustituya la primera por la segunda en la lista.
Dígame cuántas palabras tiene la lista: 4
Dígame la palabra 1: Alberto
Dígame la palabra 2: Carmen
Dígame la palabra 3: Benito
Dígame la palabra 4: Carmen
La lista creada es: ['Alberto', 'Carmen', 'Benito', 'Carmen']
Sustituir la palabra: Carmen
por la palabra: David
La lista es ahora: ['Alberto', 'David', 'Benito', 'David']
"""
lista=[]
z=int(input("Escribe cuantas palabras tiene la lista: "))
for i in range (z):
    print("Dígame una palabra: ", i+1)
    palabra=input()
    lista.append(palabra)
print("La lista creada es: ", lista)

palabra1=input("La primera palabra: ")
palabra2=input("La segunda palabra: ")
for i in range(len(lista)):
    if lista[i]==palabra1:
        lista[i]=palabra2
print(lista)