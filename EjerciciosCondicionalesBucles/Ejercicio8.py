"""
#8.	Escriba un programa que pida primero un número par y luego un número impar (positivos o negativos). 
# En caso de que uno o los dos valores no sea correcto, se mostrará un único aviso.
PAR E IMPAR (1)
Escriba un número par: -42
Escriba un número impar: 55
¡Gracias por su colaboración!
PAR E IMPAR (1)
Escriba un número par: 4
Escriba un número impar: 4
Uno o más de los valores que ha escrito no son correctos.
Ejecute de nuevo el programa para volver a intentarlo.
PAR E IMPAR (1)
Escriba un número par: 9
Escriba un número impar: 2
Uno o más de los valores que ha escrito no son correctos.
Ejecute de nuevo el programa para volver a intentarlo.
"""
x=int(input("Escribe un número par: "))
y=int(input("Escribe un número impar: "))
if x%2==0 and y%2!=0:
    print("¡Gracias por su colaboración!")
else:
    print("Ejecute de nuevo elprograma para volver a intentarlo")