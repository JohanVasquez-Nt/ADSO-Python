def sumar(num1,num2):
    return (num1+num2)
def restar(num1,num2):
    return(num1-num2)
def multiplicar(num1,num2):
    return(num1*num2)
def dividir(num1,num2):
    return(num1/num2)

while True:
    print("Menu de opciones")
    print("1. Suma ")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")
    
    confirmador = int(input("Indique la opcion: "))
    num1 = float(input("Indique el primer numero: "))
    num2 = float(input("Indique el segundo numero: "))
    
    if confirmador == 1:
        print("Usted ha seleccionado SUMA")
        print(f"El resultado de la suma es {sumar(num1,num2)}")

    if confirmador == 2:
        print("Usted ha seleccionado RESTA")
        print(f"El resultado de la suma es {restar(num1,num2)}")
        
    if confirmador == 3:
        print("Usted ha seleccionado MULTIPLICACION")
        print(f"El resultado de la suma es {multiplicar(num1,num2)}")
        
    if confirmador == 4:
        print("Usted ha seleccionado DIVISION")
        print(f"El resultado de la suma es {dividir(num1,num2)}")
        
    if confirmador == 5:
        print("Usted ha seleccionado SALIR, gracias.")
        break