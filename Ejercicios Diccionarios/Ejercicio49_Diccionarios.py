diccionario_empleados = {}
neto = 0

limite = int(input("Indique la cantidad de empleados: "))
print("-"*50)

for _ in range(limite):
    diccionario_empleados.update({int(input("Numero de id: ")) : int(input("Salario del empleado: "))})
    print("")
print("-"*50)

lista_salarios = list(diccionario_empleados.values())

for salario in lista_salarios:
    neto += salario

print(f"Salario promedio: {neto/len(lista_salarios):.2f}")