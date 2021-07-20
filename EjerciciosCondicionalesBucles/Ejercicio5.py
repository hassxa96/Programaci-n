"""
# 5. Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, 
# los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
Salida:
Introduce un número ganador:  46
Introduce un número ganador:  25
Introduce un número ganador:  32
Introduce un número ganador:  15
Introduce un número ganador:  9
Introduce un número ganador:  21
Los números ganadores son [9, 15, 21, 25, 32, 46]
"""
numeros=[] #Creación de lista vacía
for x in range (6):
    numero = int(input("Escribe un número: "))
    numeros.append(numero)
numeros.sort()
print ("Los números ganadores son: " + str(numeros))