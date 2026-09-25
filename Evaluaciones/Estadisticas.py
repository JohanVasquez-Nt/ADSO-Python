lista_ventas = []
promedio = 0
contador = 0

limite = int(input("Indique la cantidad de dias que desea registrar: "))

for _ in range(limite):
    ventas = float(input("Indique la venta del dia: "))
    lista_ventas.append(ventas)
    print("-"*50)
    
vent_max = max(lista_ventas)
vent_min = min(lista_ventas)

for venta in lista_ventas:
    promedio += venta
total = promedio
promedio = promedio / len(lista_ventas)

for venta in lista_ventas:
    if venta > promedio:
        contador += 1

print("-"*50)

print(f"""Temperatura maxima: {vent_max}
      Temperatura minima: {vent_min}
      Total vendido: {total}
      Promedio: {promedio}
      Dias por encima del promedio {contador}""")