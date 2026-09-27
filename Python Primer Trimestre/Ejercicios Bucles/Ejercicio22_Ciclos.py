limite = int(input("Indique un numero positivo: "))

for i in range(limite):
    i += 1
    if i % 2 == 0:
        print(i, end=", ")