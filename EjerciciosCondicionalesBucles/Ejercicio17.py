"""
17.	Escriba un programa que pida un número entero mayor que cero y que escriba sus divisores.
•	Un número es divisible por otro cuando el resto de su división es cero (numero % divisor == 0).
•	Se puede hacer un programa más rápido, teniendo en cuenta que los divisores son siempre menores o 
iguales que la mitad del número (salvo el propio número, que es divisor de sí mismo). Es decir, no hace 
falta probar todos los números entre 1 y el propio número, sino únicamente hasta la mitad. Si se hace así, 
no hay que olvidarse de añadir el propio número a la lista de divisores.
DIVISORES
Escriba un número mayor que cero: -5
¡Le he pedido un número entero mayor que cero!
DIVISORES
Escriba un número entero mayor que cero: 200
Los divisores de 200 son 1 2 4 5 8 10 20 25 40 50 100 200
"""
numero=int(input("Escribe un número mayor que cero: "))
lista= []
if numero<=0:
    print("¡Le he pedido un número mayor que cero!")
else:
    print("Los divisores de", numero, "son: ")
    for i in range (1, numero+1):
        if numero%i==0:
            lista.append(i)
print(lista)