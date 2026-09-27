diccionario_estudiantes = {}

limite = int(input("Indique la cantidad de estudiantes a digitar: "))
print("-"*50)

for _ in range(limite):
    diccionario_estudiantes.update({int(input("Codigo del estudiante: ")) : str(input("Nombre del estudiante: "))})
    print("")
print("-"*50)

print("Listado de estudiantes:")
for codigo, nombre in diccionario_estudiantes.items():
    print(f"{codigo} -> {nombre}")