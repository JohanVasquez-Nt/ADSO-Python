kilometros = int(input("Ingrese los kilómetros recorridos: "))
litros = int(input("Ingrese los litros de combustible consumidos: "))

rendimiento = kilometros / litros

print("-"*50)
print(f"Rendimiento: {rendimiento:.2f} km/L")