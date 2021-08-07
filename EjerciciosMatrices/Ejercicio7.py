#La columna con mayor suma de una matriz

matriz=[ [1,0,5],
    [5,5,6],
    [9,8,7]]

def mayor_suma(x):
    mayor1=0
    mayor2=0
    mayor3=0
    for f in range(len(x)):
        for c in range(len(x[f])):
            if c == 0:
                mayor1+=x[f][c]
            if c == 1:
                mayor2+=x[f][c]
            if c == 2:
                mayor3+=x[f][c]
    if mayor1>mayor2 and mayor1>mayor3:
        print("La primera columna tiene la mayor suma")
    elif mayor2>mayor3 and mayor2>mayor1:
        print("La segunda columna tiene la mayor suma")
    elif mayor3>mayor1 and mayor3>mayor2:
        print("La tercera columna tiene la mayor suma")

mayor_suma(matriz)


