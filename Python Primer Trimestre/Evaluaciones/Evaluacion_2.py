horas = int(input("Ingrese la cantidad de horas: "))
fidel = str(input("Usted pertenece al programa de fidelizacion? (S/N): ")).upper()

if horas <= 2 and fidel == "S":
    total = (6000 * horas)
    total = total - (total * 0.10)

elif horas <= 2 and fidel == "N":
    total = 6000 * horas

elif horas > 2 and horas <= 5 and fidel == "S":
    total = (5500 * horas)
    total = total - (total * 0.10)

elif horas > 2 and horas <= 5 and fidel == "N":
    total = 5500 * horas

elif horas > 5 and fidel == "S":
    total = (5000 * horas)
    total = total - (total * 0.10)
    if total >= 36000:
        total -=  (total * 0.05)

elif horas > 5 and fidel == "N":
    total = (5000 * horas)
    if total >= 40000:
        total = total - (total * 0.5)

print(f"Valor a pagar: {total:.0f}")