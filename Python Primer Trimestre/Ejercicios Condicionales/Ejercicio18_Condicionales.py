l1 = int(input("Ingrese el primer lado del triángulo: "))
l2 = int(input("Ingrese el segundo lado del triángulo: "))
l3 = int(input("Ingrese el tercer lado del triángulo: "))

print("-"*50)

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print("Sí es posible formar un triángulo.")
else:
    print("No es posible formar un triángulo.")