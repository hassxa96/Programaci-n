#3. Pedir al usuario que ingrese un día de la semana e imprimir un mensaje si es lunes, 
# otro mensaje diferente si es viernes, otro mensaje diferente si es sábado o domingo. 
# Si el día ingresado no es ninguno de esos, imprimir otro mensaje.
dia = input("Dime un día de la semana: ")
if dia == "Lunes":
    print("Es lunes")
elif dia == "viernes":
    print ("Es viernes")
elif dia == "sabado":
    print ("Es sabado")
elif dia == "domingo":
    print ("Es domingo")
else:
    print ("Es otro dia")