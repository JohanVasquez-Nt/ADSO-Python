lista_numeros = []

limite = int(input("Indique la cantidad de numeros a digitar: "))
print("-"*50)

for i in range(limite):
    numero = int(input(f"Ingrese el numero {i+1}: "))
    lista_numeros.append(numero)

print("-"*50)
buscador = int(input("Indique el numero a buscar: "))
print("-"*50)

for i in range(limite):
    if lista_numeros[i] == buscador:
        print(f"El numero {buscador} se encuentra en la posicion {i+1}.")
