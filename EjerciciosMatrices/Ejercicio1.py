#Hacer una función que sume todos los elementos de una matriz

matriz=[[1,2,3],
        [4,5,6],
        [7,8,9]]

def suma(x):
    sumatorio=0
    for f in range(len(x)):
        for c in range(len(x[f])):
            sumatorio+=x[f][c]
    return sumatorio

print("La suma de los elementos es: ", suma(matriz))
