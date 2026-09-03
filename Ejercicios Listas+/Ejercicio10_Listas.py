precios = [50, 75, 46, 22, 80, 65, 8]
min = max = precios[0]

for precio in precios:
    if precio < min:
        min = precio
    elif precio > max:
        max = precio
  
print (f"El minimo es: {min}")
print (f"El maximo es: {max}")
