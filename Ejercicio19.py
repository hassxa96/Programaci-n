"""
19.
Una vez solicitados tres números, se presenta al usuario un menú que le permitirá elegir entre: 
visualizar los
números tal y como fueron introducidos, visualizarlos en orden creciente o visualizarlos en orden
decreciente.
(Usar únicamente if,elif,else)
Ejecución:
Primer número: 5
Segundo número: 9
Tercer número: 2
¿Cómo deseas visualizar los números introducidos?
1) Sin ordenar
2) En orden creciente
3) En orden decreciente
Elige una opción 2
2, 5, 9
"""
x=int(input("Escribe el primer número: "))
y=int(input("Escribe el segundo número: "))
z=int(input("Escribe el tercer número: "))

a=int(input("Elige una opción: "))

if a==1:
    print(x,y,z)
elif a==2:
    if x<y and x<z:
        if y<z:
            print(x,y,z)
        else:
            print(x,z,y)
    elif x>y and y<z:
        if x<z:
            print(y,x,z)
        else:
            print(y,z,x)
    else:
        if x<y:
            print(z,x,y)
        else:
            print(z,y,x)
else:
    if x<y and x<z:
        if y<z:
            print(z,y,x)
        else:
            print(y,z,x)
    elif x>y and y<z:
        if x<z:
            print(z,x,y)
        else:
            print(x,z,y)
    else:
        if x<y:
            print(y,x,z)
        else:
            print(x,y,z)