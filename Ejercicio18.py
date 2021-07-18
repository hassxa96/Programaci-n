#18.Escribir un programa que solicite el ingreso de una cantidad indeterminada de números mayores que 1, 
#finalizando cuando se reciba un cero. Imprimir la cantidad de números primos ingresados

x=int(input("Escribe un número: "))
contador=0
contador1=0
while x!=0 and x>0:
    contador=0
    for i in range(2,x+1):
        if x%i==0:
            contador+=1
    if contador==1:
        contador1+=1
    x=int(input("Escribe un número: "))
print("La cantidad de números primos es", contador1)