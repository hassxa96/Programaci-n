#Ejercicio 1: Suma de los 10 primeros números pares.

contador=0
for i in range(11):
    if i%2==0:
        contador+=i
print("La suma de los diez primeros numeros pares es", contador)