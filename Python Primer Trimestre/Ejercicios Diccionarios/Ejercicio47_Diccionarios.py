diccionario_ventas = {}

limite = int(input("Indique la cantidad de vendedores a digitar: "))
print("-"*50)

for _ in range(limite):
    diccionario_ventas.update({str(input("Nombre del vendedor: ")) : float(input("Venta del vendedor: "))})
    print("")
print("-"*50)

mejor = max(diccionario_ventas, key=lambda venta: diccionario_ventas[venta])

print(f"""Mayor vendedor:
{mejor.capitalize()} -> ${diccionario_ventas[mejor]:.0f}""")
