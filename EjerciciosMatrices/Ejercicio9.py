#Sumar diagonal secundaria de una matriz

matriz=[[1,0,2],
        [0,3,6],
        [7,8,0]
        ]

def suma_diagonal(x):
    suma=0
    longitud=(len(x))-1
    for f in range(len(x)):
        suma+=x[f][longitud-f]
    return suma

print("La suma de la diagonal secundaria es: ", suma_diagonal(matriz))