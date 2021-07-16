"""
20. Dado un número entero, decir cuántos dígitos tiene. 
Ejecución:
Dame el número: 6667
6667 tiene: 4 cifra/s
"""
x=int(input("Dame un número: "))
y=x
contador=0
while x!=0:
    x=x//10
    contador+=1
print(y, "tiene:", contador, "cifras")