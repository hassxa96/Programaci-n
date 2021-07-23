"""
Ejercicio 2 Tarea: Escribir un programa que pida números positivos al usuario. 
Mostrar el número cuya sumatoria de dígitos fue mayor y la cantidad de números cuya sumatoria de 
dígitos fue menor que 10. 
Utilizar una o más funciones, según sea necesario.
"""

def sumatoria_digitos(x):
    contador=0
    while x!=0:
        y=x%10
        contador+=y
        x=x//10
    return contador
mayor=0
y=int(input("Escribe un número positivo: "))
numero_mayor=0
contador1=0
while y>0:
    suma_digitos=sumatoria_digitos(y)
    if suma_digitos>mayor:
        mayor=suma_digitos
        numero_mayor=y
    if suma_digitos<10:
        contador1+=1
    y=int(input("Escribe un número positivo: "))
print("La suma de los dígitos de", numero_mayor, "es", mayor)
print("El total de número con sumatoria menor que 10 es", contador1)