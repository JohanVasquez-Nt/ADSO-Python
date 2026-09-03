diccionario_estudiantes = {}

limite = int(input("Indique la cantidad de estudiantes a digitar: "))
print("-"*50)

for _ in range(limite):
    diccionario_estudiantes.update({str(input("Nombre del estudiante: ")) : float(input("Nota del estudiante: "))})
    print("")
print("-"*50)

mejor = max(diccionario_estudiantes, key=lambda nombre: diccionario_estudiantes[nombre])

print(f"""El estudiante con la mejor nota es:
{mejor.capitalize()} -> {diccionario_estudiantes[mejor]:.1f}""")
