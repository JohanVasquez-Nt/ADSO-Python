limite = int(input("Indique un numero positivo y entero: "))
fact = 1

print(f"{'-'*50}")

for i in range(limite):
    i += 1
    fact *= i

print(f"El factorial de {limite} es {fact}")