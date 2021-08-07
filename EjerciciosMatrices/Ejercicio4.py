#Indicador de cuántos negativos en una matriz

matriz=[[-1,2,3],
        [4,-5,6],
        [7,-8,9],
        [-2,5,1]]

def numero_negativo(x):
    contador=0
    for f in range(len(x)):
        for c in range(len(x[f])):
            if x[f][c] <0:
                contador+=1
    return contador

print("En la", matriz, "existen", numero_negativo(matriz), "números negativos")

