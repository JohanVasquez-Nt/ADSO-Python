usuario = input("Ingrese su nombre de usuario: ")
clave = input("Ingrese su clave: ")

print("-"*50)

if usuario == "admin" and clave == "Python123":
    print("Acceso concedido.")
else:
    print("Acceso denegado.")