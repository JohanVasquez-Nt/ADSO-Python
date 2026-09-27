lista_segundos = []
promedio = 0
contador = 0

limite = int(input("Indique la cantidad de dias que desea registrar: "))

for _ in range(limite):
    ventas = float(input("Indique los segundos: "))
    lista_segundos.append(ventas)
    print("-"*50)
    
seg_max = max(lista_segundos)
seg_min = min(lista_segundos)

for segundo in lista_segundos:
    promedio += segundo
promedio = promedio / len(lista_segundos)

for segundo in lista_segundos:
    if segundo > promedio:
        contador += 1

print("-"*50)

print(f"""Temperatura maxima: {seg_min}
      Temperatura minima: {seg_max}
      Promedio: {promedio:.2f}
      Dias por encima del promedio {contador}""")