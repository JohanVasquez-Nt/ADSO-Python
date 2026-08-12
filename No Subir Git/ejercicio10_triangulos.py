#Inicio
lado1 = int(input("Ingrese el primer lado del triángulo: "))
lado2 = int(input("Ingrese el segundo lado del triángulo: "))
lado3 = int(input("Ingrese el tercer lado del triángulo: "))
print(f"{"-"*50}")

#Proceso y Salida
if lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado2 + lado3 > lado1:
    print("Los lados ingresados pueden formar un triángulo.")
    print(f"{"-"*50}")
else:
    print("Los lados ingresados no pueden formar un triángulo.")
    exit()
if lado1 == lado2 and lado2 == lado3:
    print("Los lados ingresados forman un triángulo equilátero.")
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("Los lados ingresados forman un triángulo isósceles.")
elif lado1 != lado2 and lado1 != lado3 and lado2 != lado3:
    print("Los lados ingresados forman un triángulo escaleno.")
print(f"{"-"*50}")