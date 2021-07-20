#2. Solicitar al usuario que ingrese dos números y mostrar cuál de los dos es menor. 
#Considerar el caso en que ambos números son iguales.
numero = int(input("Escribe el primer número: "))
numero2 = int(input("Escribe el segundo número: "))
if numero > numero2:
    print(numero2)
elif numero < numero2:
    print(numero)
else:
    print ("Los números son iguales")