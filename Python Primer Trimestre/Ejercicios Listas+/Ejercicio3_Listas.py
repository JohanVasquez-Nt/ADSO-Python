lista_asignaturas = []
notas_asignaturas = []
num_asignaturas = int(input("Ingrese cuantas asignaturas desea ingresar: "))
print(f"{'-'*50}")

for i in range(num_asignaturas):
    asignatura = input(f"Ingrese el nombre de la asignatura {i+1}: ")
    nota = float(input(f"Ingrese la nota de la asignatura {asignatura}: "))
    lista_asignaturas.append(asignatura)
    notas_asignaturas.append(nota)
    print(f"{'-'*50}")

print(f"{'-'*50}")
for i in range(num_asignaturas):
    print(f"En la asignatura {lista_asignaturas[i]} obtuvo la nota: {notas_asignaturas[i]}")