materias = ["Matemática", "Lengua", "Inglés", "Historia", "Geografía"]
pasadas = []

for materia in materias:
    nota = float(input(f"Ingrese la nota de la materia {materia}: "))
    if nota >= 3:
        pasadas.append(materia)

for materia in pasadas:
    materias.remove(materia)
print(f"{'-'*50}")

for materia in materias:
    print(f"La materia {materia} debe repetirla")
