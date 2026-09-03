a = int(input("Indique el primer numero: "))
b = int(input("Indique el segundo numero: "))
print(f"Sus numeros son: {a} y {b}")

c = a
a = b
b = c

print("-"*50)
print("Después del intercambio:")
print(f"Numero 1: {a}")
print(f"Numero 2: {b}")