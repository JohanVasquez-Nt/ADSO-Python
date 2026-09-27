tabla = int(input("Indique el numero entero a multiplicar: "))

print(f"{'-'*50}")

for i in range(10):
    i += 1
    resul = tabla * i
    print(f"{tabla} X {i} = {resul}")