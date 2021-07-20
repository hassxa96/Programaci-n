"""
14.
Escriba un programa que pida dos números enteros. El programa pedirá de nuevo el segundo número 
mientras no sea mayor que el primero. El programa terminará escribiendo los dos números.
NÚMERO MAYOR
Escriba un número: 6
Escriba un número mayor que 6: 6
6 no es mayor que 6. Inténtelo de nuevo: 1
1 no es mayor que 6. Inténtelo de nuevo: 8

Los números que ha escrito son 6 y 8.
"""
x=int(input("Escribe un número: "))
print("Escribe un número mayor que", x)
y=int(input())
while x>=y:
    print(y, "no es mayor que", x)
    y=int(input())
print("Los números que ha escrito son:", x, "y", y)