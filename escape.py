'''
La velocidad de escape de un planeta se define como la mínima velocidad necesaria para
salir de un planeta venciendo la gravedad.
La velocidad de escape se calcula mediante la siguiente fórmula:

: corresponde a la Velocidad de Escape en [m/s].
g: corresponde a la constante gravitacional en [m/s
2
].
r: Corresponde al radio del planeta en [m].

'''
import math

print("Calculadora velocidad de escape ")
print("Por favor, ingrese solo valores numéricos para los datos solicitados.")

try:

    r_km = float(input("ingrese el radio en [km] "))
    g = float(input ("ingrese constante g [m/s] "))

    r_m = r_km * 1000 

    v_escape = math.sqrt(2 * g * r_m)

    print(f"La velocidad de escape es {v_escape:.2f} [m/s]")

except ValueError: 
    print("Error: Por favor ingrasar solo datos numericos")
