diccionario_estudiantes = {}

limite = int(input("Indique la cantidad de estudiantes a digitar: "))
print("-"*50)

for _ in range(limite):
    diccionario_estudiantes.update({int(input("Codigo del estudiante: ")) : 
                                    {"Nombre" : str(input("Nombre estudiante: ")) , 
                                     "Edad" : int(input("Edad del estudiante: ")) , 
                                     "Carrera" : str(input("Carrera del estudiante: ")) , 
                                     "Promedio" : float(input("Promedio del estudiante: "))}})
    print("")
print("-"*50)

mejor = max(diccionario_estudiantes, key=lambda codigo : diccionario_estudiantes[codigo]["Promedio"])

print(f"""Mejor estudiante:
Codigo : {mejor}""")
for i in diccionario_estudiantes[mejor]:
    print(f"{i} : {diccionario_estudiantes[mejor][i]}")
