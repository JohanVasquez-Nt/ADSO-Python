precio = int(input("Ingrese el precio del producto: "))
descuento = int(input("Ingrese el porcentaje de descuento: "))

descuento_aplicado = precio * (descuento / 100)
precio_final = precio - descuento_aplicado

print("-"*50)
print(f"Precio original: {precio}")
print(f"Descuento aplicado: {descuento_aplicado}")
print(f"Precio final: {precio_final}")