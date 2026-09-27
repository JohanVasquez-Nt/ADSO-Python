palabra = str(input("Ingrese una palabra: "))
contrario = palabra

palabra = list(palabra)
contrario = list(contrario)
contrario.reverse()

if palabra == contrario:
    print("Su palabra es un palindromo")
else:
    print("Su palabra no es un palindromo")

