diccionario_biblioteca = {}

limite = int(input("Indique la cantidad de libros a digitar: "))
print("-"*50)

for _ in range(limite):
    diccionario_biblioteca.update({str(input("Codigo del libro: ").capitalize()) : str(input("Nombre del libro: ").title())})
    print("")
print("-"*50)

codigo_libro = str(input("Indique el codigo del libro a buscar: ").capitalize())

if codigo_libro in diccionario_biblioteca:
    print(f"{codigo_libro} -> {diccionario_biblioteca[codigo_libro]}")