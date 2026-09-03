diccionario_contactos = {}

limite = int(input("Indique la cantidad de contactos a digitar: "))
print("-"*50)

for _ in range(limite):
    diccionario_contactos.update({str(input("Nombre del Contacto: ")).lower() : int(input("Numero del Contacto: "))})
    print("")
print("-"*50)

contacto = (str(input("Indique el nombre del contacto a buscar: ").lower))
busqueda = diccionario_contactos.get(contacto)
print("-"*50)

print(f"Telefono de {contacto.title}: {busqueda}")