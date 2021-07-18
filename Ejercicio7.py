#7. Crea un diccionario donde la clave sea el nombre del usuario y el valor sea el teléfono 
# (no es necesario validar). Tendrás que ir pidiendo contactos hasta el usuario diga que no quiere 
# insertar mas. 
#No se podrán meter nombres repetidos.

diccionario={}
salir=False
while salir==False:
    x=input("Escribe un nombre: ")
    y=input("Escribe un número de teléfono: ")

    if x not in diccionario:
        diccionario[x]=y
    else:
        print("El nombre está repetido")
    respuesta=input("¿Quieres salir?¡S/N!")   
    if respuesta=="S":
        salir=True
print(diccionario)