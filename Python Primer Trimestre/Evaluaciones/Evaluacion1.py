numeros_limite = []
numeros_par = []

limite = int(input("Ingrese la cantidad de numeros: "))

for i in range(limite):
    numeros_limite.append(i+1)

for i in numeros_limite:
    if i % 2 == 0:
        numeros_par.append(i)

print(numeros_par)