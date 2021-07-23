"""
Solicitar al usuario el ingreso de números primos. La lectura 
finalizará cuando ingrese un número que no sea primo. Por cada número, 
mostrar la suma de sus dígitos. También solicitar al usuario un dígito e informar la cantidad de veces 
que aparece en el número (frecuencia). Al finalizar el programa, 
mostrar el factorial del mayor número ingresado.
"""
def sumatoria(x):
    contador=0
    while x!=0:
        y=x%10
        contador+=y
        x=x//10
    return contador
def factorial(x):
    contador=1
    for i in range(1,x+1):
        contador*=i
    return contador
def frecuencia(numero, digito):
    contador=0
    while numero!=0:
        ultimo_digito=numero%10
        if ultimo_digito==digito:
            contador+=1
        numero=numero//10
    return contador
def Primo(x):
    contador=0
    Primo=False
    for i in range(1,x+1):
        if x%i==0:
            contador+=1
    if contador==2:
        Primo=True
    return Primo
    
y=int(input("Escribe un número primo: "))
mayor=0
while Primo(y)==True:
    print("La sumatoria de los dígitos de", y, "es", sumatoria(y))
    z=int(input("Introduce un dígito: "))
    print("El dígito", z, "aparece", frecuencia(y,z), "veces en el número", y)
    if y>mayor:
        mayor=y
    y=int(input("Escribe un número primo: "))
print("El factorial de", mayor, "es", factorial(mayor))