valor = float(input("Ingrese el valor de la compra: "))
descuento = 0

print("-"*50)

if valor > 500000:
    descuento = valor * 0.10
    valor = valor - descuento


print(f"Descuento: ${descuento:.0f}.")
print(f"Total a pagar: ${valor:.0f}.")