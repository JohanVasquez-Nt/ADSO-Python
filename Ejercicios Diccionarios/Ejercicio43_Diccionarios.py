diccionario_productos = {}

limite = int(input("Indique la cantidad de productos a digitar: "))
print("-"*50)

for _ in range(limite):
    diccionario_productos.update({str(input("Nombre del producto: ")).lower() : int(input("Cantidad del producto: "))})
    print("")
print("-"*50)

producto = (str(input("Indique el nombre del producto a buscar: ")).lower())
print("-"*50)

print(f"Cantidad disponible de {producto.title()}: {diccionario_productos.get(producto)}")