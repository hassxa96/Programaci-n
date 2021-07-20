"""
11. Escriba un programa que pida una cantidad de segundos y que escriba cuántos minutos y segundos son.
CONVERTIDOR DE SEGUNDOS A MINUTOS
Escriba una cantidad de segundos: 1234
1234 segundos son 20 minutos y 34 segundos
CONVERTIDOR DE SEGUNDOS A MINUTOS
Escriba una cantidad de segundos: 120
120 segundos son 2 minutos y 0 segundos
"""
x=int(input("Escribe una cantidad de segundos: "))
print(x, "segundos son", x//60, "minutos y", x%60, "segundos")