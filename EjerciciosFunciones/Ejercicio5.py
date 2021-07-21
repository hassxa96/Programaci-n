"""
Crear una función que sea capaz de determinar 
con base en el valor de los lados, el tipo de triángulo que es y calcular su perímetro.
"""

def funcion (x,y,z):
    if x==y and x==z:
        print("El triángulo es equilátero")
    elif x!=y and x!=z:
        print("El triángulo es escaleno")
    else:
        print("El triángulo es isóceles")
    return x+y+z

print("El perímetro es: ", funcion(5,4,2))
    
