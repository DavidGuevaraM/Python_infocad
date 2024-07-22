'''

'''

print("Calculadora de utilidades v03")
print("Por favor, ingrese solo valores numéricos para los datos solicitados.")

try:

    P = float(input("Ingrese el precio de suscripción: "))
    U = int(input("Ingrese el nuero de usuarios: "))
    GT = float(input("Ingrese los gastos totales: "))
    Uanterior = float(input("Ingrese la ultidad generada el año anterior: "))

    utilidades = P * U - GT

    razon = utilidades / Uanterior 

    print(f"Segun los datos ingresados, la ultildad de este año correspode a: {utilidades}")
    print(f"La razón generada entre el año anterior y el acual es de: {razon}")

except ValueError: 
    print("Error: Por favor ingrasar solo datos numericos")



