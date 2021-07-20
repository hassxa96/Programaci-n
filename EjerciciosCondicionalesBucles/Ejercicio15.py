"""
15.Escriba un programa que pida números decimales mientras el usuario escriba número mayores que el 
primero.
NÚMEROS MAYORES
Escriba un número: 7
Escriba un número mayor que 7.0: 1

1.0 no es mayor que 7.0.
NÚMEROS MAYORES
Escriba un número: 9.3
Escriba un número mayor que 9.3: 9.3

9.3 no es mayor que 9.3.
NÚMEROS MAYORES
Escriba un número: 4.5
Escriba un número mayor que 4.5: 5
Escriba otro número mayor que 4.5: 7.3
Escriba otro número mayor que 4.5: 2
2.0	no es mayor que 4.5.
"""
x=float(input("Escribe un número: "))
print("Escribe un número mayor que", x)
y=float(input())

while x<y:
    print("Escriba un número mayor que", x)
    y=float(input())
print(y,"no es mayor que", x)