lista_numeros = []

limite = int(input("Indique la cantidad de numeros a digitar: "))
print("-"*50)

for i in range(limite):
    numero = int(input(f"Ingrese el numero {i+1}: "))
    lista_numeros.append(numero)
print("-"*50)

lista_numeros.sort()

print(f"El segundo numero mayor es: {lista_numeros[i-1]}")