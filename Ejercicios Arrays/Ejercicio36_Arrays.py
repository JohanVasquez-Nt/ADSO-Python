lista_numeros = []
lista_filtrada = []

limite = int(input("Indique la cantidad de numeros a digitar: "))
print("-"*50)

for i in range(limite):
    numero = int(input(f"Ingrese el numero {i+1}: "))
    lista_numeros.append(numero)

for numero in lista_numeros:
    if numero not in lista_filtrada:
        lista_filtrada.append(numero)
print("-"*50)

print("Lista sin elementos repetidos: ")
for i in lista_filtrada:
    print(i)
