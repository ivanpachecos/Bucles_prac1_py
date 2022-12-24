"""
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual y el número de años, y muestre por pantalla el capital obtenido en la inversión cada año que dura la inversión.
"""

cantidad = float(input("Ingrese el número: "))
interes = float(input("Interes anuales: "))
nub_year = int(input("Ingrese los años: "))

for i in range (nub_year):
    cantidad *= 1 + interes/100
    print("Capital tras " + str(i+1) + " años: " + str(round(cantidad, 2)))