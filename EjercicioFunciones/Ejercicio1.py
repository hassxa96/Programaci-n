
#1.¿Qué salida escribirá el siguiente programa?
def subrutina():
    global a
    print(a)
    a += 10
    return

a = 33
subrutina()
print(a)


#33
#43