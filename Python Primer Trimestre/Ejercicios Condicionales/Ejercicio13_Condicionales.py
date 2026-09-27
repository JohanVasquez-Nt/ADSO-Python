numero = int(input("Ingrese un número: "))

print("-"*50)

if numero > 0:
    print(f"El número {numero} es positivo.")
elif numero < 0:
    print(f"El número {numero} es negativo.")
else:
    print(f"El número {numero} es cero.")