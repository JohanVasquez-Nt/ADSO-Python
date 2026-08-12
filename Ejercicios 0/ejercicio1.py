#entradas
productoprecio = float(input("Ingrese el precio del producto: "))
productoiva = float(input("Ingrese el porcentaje de IVA del producto (sin su signo): "))

#proceso
if productoiva > 100:
    preciototal = productoprecio + productoiva
else:
    preciototal = productoprecio + (productoprecio * (productoiva / 100)) 

#salidas
print("-------------------------------------------------")
print("El precio total del producto con IVA es: ", preciototal)