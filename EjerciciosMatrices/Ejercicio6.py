#Hallar la fila con más ceros

matriz=[[1,0,3],
        [0,5,6],
        [7,8,0]]

def matriz_ceros(x):
    contador1=0
    contador2=0
    contador3=0
    for c in range(3):
        if x[0][c] == 0:
            contador1+=1
            print("Incrementado el 1")
        if x[1][c] == 0:
            contador2+=1
            print("Incrementando el 2")
        if x[2][c] == 0:
            contador3+=1
            print("Incrementado el 3")
        print("Siguiente vuelta")
    print(contador1)
    print(contador2)
    print(contador3)
    if contador1>contador2 and contador1>contador3:
        print("La primera fila es la que más ceros tiene")
    elif contador2>contador3 and contador2>contador1:
        print("La segunda fila es la que más ceros tiene")
    elif contador3>contador2 and contador3>contador1:
        print("La tercera fila es la que más ceros tiene")
    else:
        print("Hay filas que tienen los mismos ceros")
    
matriz_ceros(matriz)