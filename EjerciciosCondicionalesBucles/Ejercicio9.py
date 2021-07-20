"""
Escriba un programa que pida el año actual y un año cualquiera y que escriba cuántos años han pasado desde 
ese año o cuántos años faltan para llegar a ese año.
COMPARADOR DE AÑOS
¿En qué año estamos?: 2019
Escriba un año cualquiera: 2024
Para llegar al año 2024 faltan 5 años.
COMPARADOR DE AÑOS
¿En qué año estamos?: 2019
Escriba un año cualquiera: 1997
Desde el año 1997 han pasado 22 años.
COMPARADOR DE AÑOS
¿En qué año estamos?: 2019
Escriba un año cualquiera: 2019
¡Son el mismo año!
"""
x=int(input("Escribe el año actual: "))
y=int(input("Escribe un año cualquiera: "))
if x>y:
    print("Desde el año", y, "han pasado", x-y, "años")
elif x<y:
    print("Para llegar al año", x, "faltan", y-x, "años")
else:
    print ("¡Son el mismo año!")