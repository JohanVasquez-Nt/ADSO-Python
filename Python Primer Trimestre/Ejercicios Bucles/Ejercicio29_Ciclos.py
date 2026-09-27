numero = int(input("Ingrese un numero entero positivo: "))
verificador = 0

for i in range(numero):
    i += 1
    if numero % i == 0:
        verificador += 1

if verificador == 2:
    print(f"El numero {numero} es primo")
else:
    print(f"El numero {numero} no es primo")