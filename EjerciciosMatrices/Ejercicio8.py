#Sumar diagonal principal de una matriz

matriz=[[1,0,3],
        [0,9,6],
        [7,8,0]]

def suma_diagonal(x):
    suma=0
    for f in range(len(x)):
        suma+=x[f][f]

    return suma

print("La suma de la diagonal principal es: ", suma_diagonal(matriz))