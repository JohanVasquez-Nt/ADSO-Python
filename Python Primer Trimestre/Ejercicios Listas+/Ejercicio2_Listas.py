asignaturas = []

for i in range(5):
    asignatura = input("Ingrese el nombre de la asignatura: ")
    asignaturas.append(asignatura)

print(f"{'-'*50}")

for i in range(5):
    print(f"Las asignaturas que yo estudio son: {i+1}.{asignaturas[i]}")