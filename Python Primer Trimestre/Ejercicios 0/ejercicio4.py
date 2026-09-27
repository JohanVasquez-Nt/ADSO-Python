#Entradas
num = int(input('Indique un numero entero de dos digitos: '))

#Proceso
decenas = int(num/10)
unidad = int(num-(decenas*10))

#Salidas
print("El numero que coloco es: ",num)
print("Su decena es: ",decenas)
print("La unidad es: ",unidad)