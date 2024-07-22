'''
Actividad 2 - Rentabilidad
Un emprendedor quiere crear una app que provea un servicio de entrega de comida para
mascotas. Este proyecto tiene buenos pronósticos, pero su éxito dependerá de cuántos
usuarios pueda alcanzar. La manera en la que se medirá esto es calculando las utilidades
del proyecto. Estas utilidades se pueden calcular mediante la siguiente fórmula:
𝑈𝑡𝑖𝑙𝑖𝑑𝑎𝑑𝑒𝑠 = 𝑃 * 𝑈 − 𝐺𝑇
Donde:
P: Precio de Suscripción
U: Número de Usuarios
GT: Gastos Totales

'''

print("Calculadora de utilidades v01")
print("Por favor, ingrese solo valores numéricos para los datos solicitados.")

try:
    P = float(input("Ingrese el precio de suscripción: "))
    U = int(input("Ingrese el nuero de usuarios: "))
    GT = float(input("Ingrese los gastos totales: "))

    utilidades = P * U - GT

    print(f"Segun los datos ingresados, la ultildad correspode a: {utilidades}")

except ValueError: 
    print("Error: Por favor ingrasar solo datos numericos")

