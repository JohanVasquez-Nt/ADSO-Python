lista_numeros = []

limite = int(input("Indique la cantidad de numeros a digitar: "))
print("-"*50)

for i in range(limite):
    numero = int(input(f"Ingrese el numero {i+1}: "))
    lista_numeros.append(numero)
lista_arreglada = lista_numeros[:]
print("-"*50)

for _ in range(limite):
    for j in range(limite - 1):
        if lista_arreglada[j] > lista_arreglada[j+1]:
            lista_arreglada[j] , lista_arreglada[j+1] = lista_arreglada[j+1] , lista_arreglada[j]

print("Lista ordenada:")
for i in lista_arreglada:
    print(i)
