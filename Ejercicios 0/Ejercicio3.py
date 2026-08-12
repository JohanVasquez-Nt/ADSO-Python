#Inicio
kmdistancia = float(input('Indique el numero de Km recorridos por su coche: '))
lconsumidos = float(input('Indique el numero de Litros consumidos por su coche: '))

#Procesos
kmconsumo =  kmdistancia / lconsumidos

#Salidas
print ("Su coche ha recorrido: " ,kmdistancia, "km y ha gastado:" ,lconsumidos, "Litros")
print ("Su coche consume:" ,kmconsumo, "Litros por Km")
