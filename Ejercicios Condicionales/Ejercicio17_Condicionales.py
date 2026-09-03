print("Opciones disponibles:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

print("-"*50)

confirmador = int(input("Ingrese la opción deseada (1-4): "))
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if confirmador == 1:
    resultado = num1 + num2
    print(f"El resultado de la suma es: {resultado:.0f}.")
elif confirmador == 2:
    resultado = num1 - num2
    print(f"El resultado de la resta es: {resultado:.0f}.")
elif confirmador == 3:
    resultado = num1 * num2
    print(f"El resultado de la multiplicación es: {resultado:.0f}.")
elif confirmador == 4:
    if num2 != 0:
        resultado = num1 / num2
        print(f"El resultado de la división es: {resultado:.0f}.")
    else:
        print("Error: No se puede dividir entre cero.")