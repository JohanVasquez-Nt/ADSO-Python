vocal = 0

palabra = str(input("Indique una palabra o frase: "))

for i in palabra:
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        vocal += 1

print(f"La palabra contiene {vocal} vocales")
