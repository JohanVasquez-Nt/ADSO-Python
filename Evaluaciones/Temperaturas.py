lista_temperaturas = []
promedio = 0
contador = 0

for _ in range(7):
    temperatura = float(input("Indique la temperatura de hoy: "))
    lista_temperaturas.append(temperatura)
    print("-"*50)
    
temp_max = max(lista_temperaturas)
temp_min = min(lista_temperaturas)

for temperatura in lista_temperaturas:
    promedio += temperatura
promedio = promedio / len(lista_temperaturas)

for temperatura in lista_temperaturas:
    if temperatura > promedio:
        contador += 1

print("-"*50)

print(f"""Temperatura maxima: {temp_max}°C
      Temperatura minima: {temp_min}°C
      Promedio: {promedio}°C
      Dias por encima del promedio {contador}""")