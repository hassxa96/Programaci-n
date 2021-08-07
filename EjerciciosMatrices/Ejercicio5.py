#Indicador de si existen negativos en una matriz

matriz=[[1,2,3],
        [4,5,6],
        [7,8,9],
        [-1,3,7]]

def numero_negativo(x):
    numero=False
    for f in range(len(x)):
        for c in range(len(x[f])):
            if x[f][c] <0:
                return True
    return numero

print("En la", matriz, "existen negativos: ", numero_negativo(matriz))