"""
12.Escriba un programa que pida números mientras no se escriba un número negativo. 
El programa terminará escribiendo la suma de los números introducidos.
SUMA DE NÚMEROS
Escriba un número: -4

La suma de los números positivos introducidos es 0.
SUMA DE NÚMEROS
Escriba un número: 12
Escriba otro número: 3
Escriba otro número: 0
Escriba otro número: 7
Escriba otro número: -1

La suma de los números positivos introducidos es 22.
"""
contador=0
z=int(input("Escribe un número: "))
contador+=z
while z>=0:
    z=int(input("Escribe otro número: "))
    if z>=0:
        contador+=z
print("La suma de los números positicos introducidos es: ", contador)