lista_palabras = []

limite = int(input("Indique la cantidad de palabras a digitar: "))
print("-"*50)

for i in range(limite):
    palabra = str(input(f"Indique la palabra {i+1}: "))
    lista_palabras.append(palabra)

print("-"*50)
lista_palabras.reverse()

print("Lista invertida:")
for i in lista_palabras:
    print(i)