limite = int(input("Indique un numero positivo: "))
total = 0

for i in range(limite):
    total = (i + 1) + total

print (f"La suma de los primeros {limite} numeros es: {total}")