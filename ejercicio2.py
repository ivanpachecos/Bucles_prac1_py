"""
Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).
"""
edad = int(input("Ingrese el año: "))
for i in range(edad):
    print("Mi edad es: ", str(i+1))