"""
16.Escriba un programa que pida dos números enteros y escriba qué números son pa-res y cuáles impares desde
el primero hasta el segundo.
Un número es par cuando el resto de su división entre dos es cero (numero % 2 == 0) 
e impar cuando no lo es.
PARES E IMPARES
Escriba un número entero: 6
Escriba un número entero mayor o igual que 6: 2
¡Le he pedido un número entero mayor o igual que 6!
PARES E IMPARES
Escriba un número entero: 4
Escriba un número entero mayor o igual que 4: 8
El número 4 es par
El número 5 es impar
El número 6 es par
El número 7 es impar
El número 8 es par
PARES E IMPARES
Escriba un número entero: 5
Escriba un número entero mayor o igual que 5: 5
El número 5 es impar
"""
x=int(input("Escribe un número: "))
y=int(input("Escribe otro número: "))
if x>y:
    print("¡Le he pedido un número entero mayor o igual que", x,"!")
else:
    for i in range(x,y+1):
        if i%2==0:
            print("El número", i, "es par")
        else:
            print("El número", i, "es impar")