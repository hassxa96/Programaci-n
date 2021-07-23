"""
Solicitar al usuario un número entero y luego un dígito. Informar la cantidad de ocurrencias 
del dígito en el número, 
utilizando para ello una función que calcule la frecuencia.
"""
x=int(input("Escribe un número: "))
y=int(input("Escribe un dígito de ese número: "))
def frecuencia(numero, digito): #numero=100 y digito=0
    contador=0
    digitoNum=numero%10 #digitoNum= 0
    numero=numero//10 #numero=10
    while numero!=0:
        if digitoNum==digito:
            contador+=1 #contador=2
        digitoNum=numero%10 #digitoNum=1 
        numero=numero//10 #numero=0
    return contador
print("El número se repite", frecuencia(x,y),"veces")