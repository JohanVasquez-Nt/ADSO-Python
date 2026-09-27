num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

print("-"*50)

if num1 > num2:
    print(f"El numero mayor es: {num1}.")
elif num2 > num1:
    print(f"El numero mayor es: {num2}.")
else:
    print(f"Los dos números {num1} y {num2} son iguales.")