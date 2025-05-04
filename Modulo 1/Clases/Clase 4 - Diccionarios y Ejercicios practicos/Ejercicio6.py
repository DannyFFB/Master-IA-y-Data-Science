"""6-Una función que determine el sueldo de un empleado teniendo en cuenta mínimo dos variables"""

def sueldo ():

    diaslab = int(input("Ingrese numero de dias laborados : "))
    sueldodia = float(input("Ingrese cuanto gana al dia: "))

    Total = (diaslab * sueldodia)

    print(f"Su sueldo es de: ${Total}")

sueldo()