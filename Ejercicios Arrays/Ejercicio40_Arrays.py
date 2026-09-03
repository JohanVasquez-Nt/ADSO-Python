lista_compra = []

limite = int(input("Indique la cantidad de productos a digitar: "))
print("-"*50)

for i in range(limite):
    numero = str(input(f"Ingrese el producto {i+1}: "))
    lista_compra.append(numero)
print("-"*50)

print("Lista de compras:")
for i in range(limite):
    print(f"{i+1}. {lista_compra[i]}")