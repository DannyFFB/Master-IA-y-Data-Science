"""3-Una función que me calcule el perímetro de un cuadrado"""

def square(lado):

    perimetro = 4 * lado

    return perimetro

lado = float(input("Ingresa el lado del cuadrado: "))
print(f"El perimetro del cuadrado es: {square(lado)}")
