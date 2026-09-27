lista_numeros1 = []
lista_numeros2 = []
lista_numeros3 = []

limite = int(input("Indique la cantidad de numeros a digitar: "))
print("-"*50)

for i in range(limite):
    numero = int(input(f"Ingrese el numero {i+1} de la lista 1: "))
    lista_numeros1.append(numero)
print("-"*50)
for i in range(limite):
    numero = int(input(f"Ingrese el numero {i+1} de la lista 2: "))
    lista_numeros1.append(numero)
print("-"*50)

lista_numeros3.extend(lista_numeros1)
lista_numeros3.extend(lista_numeros2)

print("Lista combinada:")
for i in lista_numeros3:
    print(i)