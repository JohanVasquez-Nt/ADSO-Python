def depositar(valor,saldo):
    return(valor+saldo)
def retirar(valor,saldo):
    return(saldo-valor)
saldo = 1270000
contra = int(input("Indique la contraseña: "))

if contra == 1234:
    while True:
    
        print("-"*50)
        print("Menu del Cajero")
        print("1. Consultar saldo\n2. Depositar dinero\n3. Retirar dinero\n4. Transferir dinero\n5. Cancelar operacion")
        print("-"*50)
        confirmador = int(input("Indique la operacion a realizar: "))
        print("-"*50)
        
        match confirmador:
            case 1:
                print(f"Su saldo es {saldo}")
            case 2:
                valor = int(input("Indique la cantidad a depositar: "))
                print(f"El valor depositado es: {valor}, su total ahora es: {depositar(valor,saldo)}")
            case 3:
                valor = int(input("Indique la cantidad a retirar: "))
                print(f"El valor a retirar es de: {valor}, su saldo es ahora de: {retirar(valor,saldo)}")
            case 4:
                valor = int(input("Indique la cantidad a transferir: "))
                print(f"El valor a transferir es de: {valor}, su saldo es ahora de: {retirar(valor,saldo)}")
            case 5:
                print("Se ha cancelado la operacion, gracias")
                break
            case _:
                print("Seleccione una opcion valida.")

        print("-"*50) 
else:   
    print("Contraseña incorrecta")
print("-"*50)