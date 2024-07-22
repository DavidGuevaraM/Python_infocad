'''

'''

print("Calculadora de utilidades v02")
print("Por favor, ingrese solo valores numéricos para los datos solicitados.")

try:

    P = float(input("Ingrese el precio de suscripción: "))
    Unormal = int(input("Ingrese el nuero de usuarios: "))
    Upremiun = int(input("Ingrese el nuero de usuarios premiun: "))
    GT = float(input("Ingrese los gastos totales: "))

    Ppremiun = P * 1.5

    utilidades = (P * Unormal) + (Ppremiun * Upremiun) - GT

    print(f"Segun los datos ingresados, la ultildad correspode a: {utilidades}")

except ValueError: 
    print("Error: Por favor ingrasar solo datos numericos")

