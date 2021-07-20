"""
13. Escriba un programa que pida dos números enteros y que calcule su división, escribiendo si la división 
es exacta o no.
DIVISOR DE NÚMEROS
Escriba el dividendo: 14
Escriba el divisor: 5
La división no es exacta. Cociente: 2 Resto: 4
DIVISOR DE NÚMEROS
Escriba el dividendo: 20
Escriba el divisor: 4
La división es exacta. Cociente: 5
"""
x=int(input("Escribe el dividendo: "))
y=int(input("Escribe el divisor: "))

if x%y!=0:
    print("La división no es exacta. Cociente:", x//y, "Resto:", x%y)
else:
    print("La división es exacta. Cociente.", x/y)