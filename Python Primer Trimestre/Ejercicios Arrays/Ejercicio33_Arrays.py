lista_numeros = []
par , impar = 0 , 0

limite = int(input("Indique la cantidad de numeros a digitar: "))
print("-"*50)

for i in range(limite):
    numero = int(input(f"Ingrese el numero {i+1}: "))
    lista_numeros.append(numero)

for i in lista_numeros:
    if i % 2 == 0:
        par += 1
    else:
        impar += 1

print("-"*50)

print(f"Pares: {par}")
print(f"Impares: {impar}")