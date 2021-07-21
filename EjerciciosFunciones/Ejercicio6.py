#Crea una función que dados dos números mostrará todos los números que hay entre ellos

def funcion (x,y):
    for i in range(x+1,y):
        print(i)
    for i in range (y+1,x):
        print(i)
x=int(input("Escribe el primer número: "))
y=int(input("Escribe el segundo número: "))

funcion(x,y)