#entradas
horastrabajadas = input("Ingrese la cantidad de horas trabajadas: ")
valorhora = input("Ingrese el valor de las horas trabajadas: ")

#proceso
salario = float(horastrabajadas) * float(valorhora)
descuento = float(salario) * 0.12
salariototal = salario - descuento

#salidas
print("-------------------------------------------------")
print("El salario antes de descuento es: ", salario)
print("-------------------------------------------------")
print("El descuento es: ", descuento)
print("-------------------------------------------------")
print("El salario total es: ", salariototal)
print("-------------------------------------------------")
