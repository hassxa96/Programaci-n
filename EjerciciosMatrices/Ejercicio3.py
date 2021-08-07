#Suma de los elementos de una columna de una matriz

matriz=[[1,2,3],
        [4,5,6],
        [7,8,9]]

print("¿Qué columna quiere sumar?")
print("Marque 1 si la primera columna")
print("Marque 2 si la segunda columna")
print("Marque 3 si la tercera columna")
pregunta=int(input())
def suma_columna(x,pregunta):
    sumatorio=0

    for f in range(len(x[pregunta-1])):
        sumatorio+=x[f][pregunta-1]
        
    return sumatorio

print("El sumatorio de la columna seleccionada es", suma_columna(matriz,pregunta))