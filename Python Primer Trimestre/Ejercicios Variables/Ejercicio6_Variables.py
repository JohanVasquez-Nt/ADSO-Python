segundos = int(input("Indique la cantidad de segundos: "))

horas = segundos / 3600
minutos = (segundos % 3600) / 60
segundo = (segundos % 60)

print("-"*50)
print(f"{segundos} segundos equivalen a:")
print(f"{horas:.0f} hora(s)")
print(f"{minutos:.0f} minuto(s)")
print(f"{segundo:.0f} segundo(s)")