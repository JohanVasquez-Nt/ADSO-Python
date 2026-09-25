lista_deportistas = []
lista_tiempos = []

while True:
    print("")
    print("""============== MENÚ ============== 
    1. Registrar deportista 
    2. Mostrar deportistas 
    3. Buscar deportista 
    4. Mostrar mejor tiempo 
    5. Mostrar tiempo promedio 
    6. Salir 
======================================== """)
    print("")
    confirmador = int(input("Indique la opcion necesitada: "))
    print("")

    match confirmador:
        case 1:
            cantidad = int(input("Cuantos deportistas desea digitar: "))
            print("")
            for i in range(cantidad):
                lista_deportistas.append(str(input("Indique el nombre del deportista: ")))
                lista_tiempos.append(float(input("Indique el tiempo obtenido en segundos: ")))
                print("")
        case 2:
            if len(lista_deportistas) > 0:
                for i in range(len(lista_deportistas)):
                    print(f"El deportista {lista_deportistas[i]} obtuvo {lista_tiempos[i]}seg")
            else:
                print("No hay deportistas ni tiempos registrados")
        case 3:
            nombre = str(input("Indique el nombre del deportista a buscar: "))
            if nombre in lista_deportistas:
                seg = lista_deportistas.index(nombre)
                print(f"El nombre del deportista es: {nombre} sus segundos fueron: {lista_tiempos[seg]}")
            else:
                print(f"El deportista {nombre} no fue encontrado")
        case 4:
            mejor = min(lista_tiempos)
            seg = lista_tiempos.index(mejor)
            print(f"El deportista: {lista_deportistas[seg]} tuvo el mejor tiempo con: {mejor}seg")
        case 5:
            if len(lista_tiempos) > 0:
                promedio = 0
                for numero in lista_tiempos:
                    promedio += numero
                print(f"El tiempo promedio de los deportistas son: {promedio / len(lista_tiempos)}seg")
            else:
                print("No hay deportistas ni tiempos registrados")
        case 6:
            print("Usted ha seleccionado la opciona salir, hasta pronto.")
            break
        case _:
            print("Indique un numero valido")
