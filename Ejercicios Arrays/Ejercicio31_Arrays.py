lista_numeros = []

limite = int(input("Indique la cantidad de numeros a digitar: "))
print("-"*50)

for i in range(limite):
    numero = int(input(f"Ingrese el numero {i+1}: "))
    lista_numeros.append(numero)

#Forma 1
menor , mayor = i , i
for i in lista_numeros:
    if i > mayor:
        mayor = i
    if i < menor:
        menor = i

#Forma 2 (Tambien se puede hacer con .Sort)
#mayor = max(lista_numeros)
#menor = min(lista_numeros)

print(f"Mayor: {mayor}")
print(f"Menor: {menor}")

