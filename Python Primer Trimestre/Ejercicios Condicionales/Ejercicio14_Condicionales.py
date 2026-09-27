edad = int(input("Ingrese su edad: "))

print("-"*50)

if edad <= 12:
    print("Clasificacion: Niño.")
elif edad <= 17:
    print("Clasificacion: Adolescente.")
elif edad <= 59:
    print("Clasificacion: Adulto.")
else:
    print("Clasificacion: Adulto mayor.")