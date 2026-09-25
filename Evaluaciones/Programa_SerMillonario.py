def respuesta_pregunta_principal():
    answer = str(input("Indique su respuesta: ")).upper()
    if preguntas_principales[pregunta][answer] in respuestas_principales:
        print("Correcto, continue")
    else:
        print("Incorrecto, gracias por jugar.")
        return False
def respuesta_pregunta_respaldo():
    answer = str(input("Indique su respuesta: ")).upper()
    if preguntas_respaldo[pregunta_r][answer] in respuestas_respaldo:
        print("Correcto, continue")
    else:
        print("Incorrecto, gracias por jugar.")
        return False
def mostrar_ayudas():
    print(f"\nRecuerda que tienes ayudas unicas:")
    for key , value in ayudas.items():
        print(f"{key}. {value}.", end="  ")
    print("")
def ayuda_mitad():      
    if answer == "1" and answer in ayudas:
        for letra, respuesta in opciones.items():
            if respuesta not in respuestas_principales:
                print(f"{letra}. {respuesta}")
                break
        for letra, respuesta in opciones.items():
            if respuesta in respuestas_principales:
                print(f"{letra}. {respuesta}")
    ayudas.pop(answer)
def ayuda_amigo_principal():
    for letra, respuesta in opciones.items():
        if respuesta in respuestas_principales:
            print(f"Oe pana la respuesta es {respuesta}")
    ayudas.pop(answer)
def ayuda_mitad_respaldo():      
    if answer == "1" and answer in ayudas:
        for letra_r, respuesta_r in opciones_r.items():
            if respuesta not in respuestas_respaldo:
                print(f"{letra_r}. {respuesta_r}")
                break
        for letra_r, respuesta_r in opciones_r.items():
            if respuesta_r in respuestas_respaldo:
                print(f"{letra_r}. {respuesta_r}")
    ayudas.pop(answer)
def ayuda_amigo_respaldo():
    for letra_r, respuesta_r in opciones_r.items():
        if respuesta_r in respuestas_respaldo:
            print(f"Oe pana la respuesta es {respuesta_r}")
    ayudas.pop(answer)

ayudas = {"1" : "50/50",
          "2" : "Llamar a un amigo",
          "3" : "Cambiar la pregunta"}

preguntas_principales = {"Pregunta 1: \n¿Cuántos meses tiene un año?" : {
    "A" : "10",
    "B" : "11",
    "C" : "12",
    "D" : "13"},
"Pregunta 2: \n¿Cuál es la capital de Colombia?" : {
    "A" : "Cali",
    "B" : "Medellín",
    "C" : "Bogotá",
    "D" : "Cartagena"},
"Pregunta 3: \n¿Cuál es el planeta más cercano al Sol?" : {
    "A" : "Venus",
    "B" : "Marte",
    "C" : "Mercurio",
    "D" : "Tierra"},
"Pregunta 4: \n¿Quién escribió 'Don Quijote de la Mancha'?" : {
    "A" : "Gabriel García Márquez",
    "B" : "Miguel de Cervantes",
    "C" : "Pablo Neruda",
    "D" : "Lope de Vega"},
"Pregunta 5: \n¿Cuál es el océano más grande del mundo?" : {
    "A" : "Atlántico",
    "B" : "Índico",
    "C" : "Pacífico",
    "D" : "Ártico"},
"Pregunta 6: \n¿Cuál es el símbolo químico de la plata?" : {
    "A" : "Pt",
    "B" : "Ag",
    "C" : "Au",
    "D" : "Pb"},
"Pregunta 7: \n¿Quién fue el primer ser humano en viajar al espacio?" : {
    "A" : "Neil Armstrong",
    "B" : "Yuri Gagarin",
    "C" : "John Glenn",
    "D" : "Buzz Aldrin"},
"Pregunta 8: \n¿Cuál es el país más pequeño del mundo?" : {
    "A" : "Mónaco",
    "B" : "Luxemburgo",
    "C" : "Malta",
    "D" : "Ciudad del Vaticano"},
"Pregunta 9: \n¿En qué continente se encuentra el desierto del Kalahari?" : {
    "A" : "Asia",
    "B" : "África",
    "C" : "Oceanía",
    "D" : "América"},
"Pregunta 10: \n¿Cuál de estos científicos recibió dos premios Nobel en diferentes disciplinas científicas?" : {
    "A" : "Albert Einstein",
    "B" : "Niels Bohr",
    "C" : "Marie Curie",
    "D" : "Max Planck"}}
respuestas_principales = ["12" , "Bogotá" , "Mercurio" , "Miguel de Cervantes" , "Pacífico" , "Ag" , "Yuri Gagarin" , "Ciudad del Vaticano" , "África" , "Marie Curie"]

preguntas_respaldo = {
"Pregunta 1: \n¿Cuál es el animal terrestre más rápido del mundo?" : {
    "A" : "León",
    "B" : "Guepardo",
    "C" : "Tigre",
    "D" : "Antílope"},
"Pregunta 2: \n¿Cuántos lados tiene un hexágono?" : {
    "A" : "5",
    "B" : "6",
    "C" : "7",
    "D" : "8"},
"Pregunta 3: \n¿Cuál es el río más largo de Sudamérica?" : {
    "A" : "Orinoco",
    "B" : "Paraná",
    "C" : "Amazonas",
    "D" : "Magdalena"},
"Pregunta 4: \n¿Quién pintó la Mona Lisa?" : {
    "A" : "Leonardo da Vinci",
    "B" : "Pablo Picasso",
    "C" : "Vincent van Gogh",
    "D" : "Miguel Ángel"},
"Pregunta 5: \n¿Cuál es el idioma oficial de Brasil?" : {
    "A" : "Español",
    "B" : "Francés",
    "C" : "Portugués",
    "D" : "Italiano"},
"Pregunta 6: \n¿Qué instrumento se utiliza para medir la temperatura?" : {
    "A" : "Barómetro",
    "B" : "Termómetro",
    "C" : "Higrómetro",
    "D" : "Altímetro"},
"Pregunta 7: \n¿Cuál es la montaña más alta del mundo sobre el nivel del mar?" : {
    "A" : "K2",
    "B" : "Aconcagua",
    "C" : "Everest",
    "D" : "Kilimanjaro"},
"Pregunta 8: \n¿En qué año comenzó la Segunda Guerra Mundial?" : {
    "A" : "1914",
    "B" : "1939",
    "C" : "1945",
    "D" : "1929"},
"Pregunta 9: \n¿Cuál es el único mamífero capaz de volar?" : {
    "A" : "Ardilla voladora",
    "B" : "Murciélago",
    "C" : "Cóndor",
    "D" : "Pingüino"},
"Pregunta 10: \n¿Cuál es el elemento químico más abundante en el universo?" : {
    "A" : "Oxígeno",
    "B" : "Carbono",
    "C" : "Hidrógeno",
    "D" : "Helio"}}
respuestas_respaldo = ["Guepardo", "6", "Amazonas", "Leonardo da Vinci", "Portugués", "Termómetro", "Everest", "1939", "Murciélago", "Hidrógeno"]

#PREGUNTA
for pregunta, opciones in preguntas_principales.items():
    print(f"\n{pregunta}")
    for letra, respuesta in opciones.items():
        print(f"{letra}. {respuesta}")

    mostrar_ayudas()

    indicativo = str(input("Desea responder la pregunta? (1. Si ; 2. Quiero usar una ayuda)\nR. "))

    match indicativo:
        case "1":
            if respuesta_pregunta_principal() == False:
                break

        case "2":
            answer = str(input("Indique cual ayuda desea: "))

            if answer == "1" and answer in ayudas:
                ayuda_mitad()

                if respuesta_pregunta_principal() == False:
                    break

            elif answer == "2" and answer in ayudas:
                ayuda_amigo_principal()
                if respuesta_pregunta_principal() == False:
                    break

            elif answer == "3" and answer in ayudas:
                ayudas.pop(answer)

                for i, (pregunta_r, opciones_r) in enumerate(preguntas_respaldo.items(), start=1):
                    if str(i) in pregunta:
                        print(f"\n{pregunta_r}")

                        for letra_r, respuesta_r in opciones_r.items():
                            print(f"{letra_r}. {respuesta_r}")

                        mostrar_ayudas()

                        indicativo = str(input("Desea responder la pregunta? (1. Si ; 2. Quiero usar una ayuda)\nR. "))

                        match indicativo:
                            case "1":
                                resp = respuesta_pregunta_respaldo()
                            case "2":
                                answer = str(input("Indique cual ayuda desea: "))

                                if answer == "1" and answer in ayudas:
                                    ayuda_mitad_respaldo()
                                    resp = respuesta_pregunta_respaldo()

                                elif answer == "2" and answer in ayudas:
                                    ayuda_amigo_respaldo()
                                    resp = respuesta_pregunta_respaldo()
                                    
                if resp == False:
                    break
            else:
                print("Mi loco avispate un poco.")
                break
        case _:
            print("\nIndicaste un caso invalido, bye.")
            break


