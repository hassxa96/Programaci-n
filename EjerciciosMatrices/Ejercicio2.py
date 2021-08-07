#Suma de los elementos de una fila de una matriz

matriz=[[1,2,3],
        [4,5,6],
        [7,8,9],
        [2,3,1]]
print("¿Qué fila quiere sumar?")
print("Marque 1 si la primera fila")
print("Marque 2 si la segunda fila")
print("Marque 3 si la tercera fila")
print("Marque 4 si la cuarta fila")
pregunta=int(input())
def suma_fila(x,pregunta):
    sumatorio=0

    for c in range(len(x[pregunta-1])):
        sumatorio+=x[pregunta-1][c]
        
    return sumatorio

print("El sumatorio de la fila seleccionada es", suma_fila(matriz,pregunta))