"""4-Una función que determine si un número digitado por el usuario es par o no"""

def num(numUser):

    if numUser % 2 == 0:
     print("El numero es par")
    else:
     print("El numero es impar")

User = int(input("Ingrese numero : "))

num(User)
