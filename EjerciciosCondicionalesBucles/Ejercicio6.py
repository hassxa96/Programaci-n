#6. Crea una tupla con números, pide un numero por teclado e 
# indica cuantas veces se repite ese número en la tupla creada.
tuple= (1,2,3,4,5,5,2,4)
x=int(input("Escribe un número: "))
contador=0
for i in tuple:
    if i==x:
        contador+=1
print("EL número se repite:", contador)