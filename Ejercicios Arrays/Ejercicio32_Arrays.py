lista_notas = []
promedio = 0

limite = int(input("Indique la cantidad de notas a digitar: "))
print("-"*50)

for i in range(limite):
    nota = float(input(f"Ingrese la nota {i+1}: "))
    lista_notas.append(nota)

for i in range(limite):
    promedio += lista_notas[i]
promedio /= limite

print(f"Promedio: {promedio:.2f}")