limite = int(input("Indique la cantidad de numeros a ingresar: "))
positivo = 0
negativo = 0
cero = 0

print(f"{'-'*50}")

for i in range(limite):
    numero = int(input("Indique el numero: "))
    if numero == 0:
        cero += 1
    elif numero >= 1:
        positivo += 1
    elif numero < 0:
        negativo += 1
    print(f"{'-'*50}")
    
print(f"Positivos: {positivo}")
print(f"Negativos: {negativo}")
print(f"Ceros: {cero}")

