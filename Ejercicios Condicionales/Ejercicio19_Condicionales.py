l1 = int(input("Ingrese el primer lado del triángulo: "))
l2 = int(input("Ingrese el segundo lado del triángulo: "))
l3 = int(input("Ingrese el tercer lado del triángulo: "))

print("-"*50)

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print("Sí es posible formar un triángulo.")
else:
    print("No es posible formar un triángulo.")

print("-"*50)
print("Clasificación del triángulo según sus lados:")

if l1 == l2 and l2 == l3:
    print("El triángulo es Equilátero.")
elif l1 == l2 or l1 == l3 or l2 == l3:
    print("El triángulo es Isósceles.")
else:
    print("El triángulo es Escaleno.")