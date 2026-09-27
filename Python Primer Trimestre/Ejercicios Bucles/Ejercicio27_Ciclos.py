limite = int(input("Indique el limite a sumar: "))
total = 0

for i in range(limite):
    i += 1
    if i % 2 != 0:
        total += i

print(f"La suma de los numeros impares es: {total}")