lista_ganadores = []

for i in range(5):
    numero = int(input("Ingrese un número ganador: "))
    lista_ganadores.append(numero)

print(f"{'-'*50}")

lista_ganadores.sort()
print("Los números ganadores ordenados de menor a mayor son:")
for i in range(5): 
    print(f"{i+1}. {lista_ganadores[i]}")