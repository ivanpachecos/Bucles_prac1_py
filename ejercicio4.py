"""
Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla la cuenta atrás desde ese número hasta cero separados por comas.
"""
x = int(input("Ingrese el número positivo: "))

for i in range(x, -1, -1):
    print(i, end=", ")