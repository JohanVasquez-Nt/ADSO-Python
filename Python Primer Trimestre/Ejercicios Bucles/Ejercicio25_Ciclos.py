limite = int(input("Indique la cantidad de notas: "))
nota = 0

print(f"{'-'*50}")

for i in range(limite):
    notas = float(input("Indique la nota: "))
    nota = nota + notas
    print(f"{'-'*50}")

print(f"El promedio de las notas es: {nota/limite:.2f}")
