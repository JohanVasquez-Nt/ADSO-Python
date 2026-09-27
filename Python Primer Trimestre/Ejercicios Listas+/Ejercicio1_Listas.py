asignaturas = []

for i in range(5):
    asignatura = input("Ingrese el nombre de la asignatura: ")
    asignaturas.append(asignatura)

print(f"{'-'*50}")

print("Las asignaturas ingresadas son:")
for i in range(5):
    print(f"{i+1}- {asignaturas[i]}")