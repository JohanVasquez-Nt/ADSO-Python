fib = [0, 1]

limite = int(input("Ingrese la cantidad de terminos que desea generar: "))

while len(fib) < limite:
       fib.append(fib[-1] + fib[-2])

print(fib)