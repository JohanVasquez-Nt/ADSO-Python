nombre = str(input("Indique su nombre: "))
horas_trab = int(input("Indique la cantidad de horas trabajadas: "))
valor_hora = float(input("Indique el valor de la hora: "))

print(f"-"*50)

print(f"Empleado: {nombre}")
print(f"Horas trabajadas: {horas_trab}")
print(f"Valor por hora: {valor_hora:.0f}")
print(f"Salario total: {horas_trab * valor_hora:.0f}")