#Inicio
print("------------------------------------------------------------------------")
nombremascota = str(input("Ingrese el nombre de la mascota: "))
nombrecomun = str(input("Ingrese el nombre común: "))
edadmascota = int(input("Ingrese la edad (en años) de la mascota: "))
nombredueño = str(input("Ingrese el nombre del dueño de la mascota: "))
print("------------------------------------------------------------------------")
procedimiento = str(input("Ingrese el procedimiento que se le realizó a la mascota: "))
precio = float(input("Ingrese el precio del procedimiento: "))
cantidad = int(input("Ingrese la cantidad de veces que se realizó el procedimiento: "))

#Proceso
subtotal = 0
precioxunidad = precio * cantidad
total = precioxunidad + (precioxunidad * 0.19)

#Salida
print("--------------------FACTURA DE VETERINARIA------------------------------")
print("Nombre de la mascota:", nombremascota)
print("Nombre común de la mascota:", nombrecomun)
print("Edad de la mascota:", edadmascota)
print("Nombre del dueño de la mascota:", nombredueño)
print("------------------------------------------------------------------------")
print("Descripción del procedimiento:" ,procedimiento, "| Cantiad de veces que se realizó el procedimiento:", cantidad, "| Precio del procedimiento:", precio, "| Precio total del procedimiento:", precioxunidad)
print("------------------------------------------------------------------------")
print("Total a pagar (con IVA): ", total)