"""Escribir un programa que pida al usuario un número entero positivo y muestre por pantalla todos los números impares desde 1 hasta ese número separados por comas."""
numb = int(input("Ingrese el número: "))
for i in range(1, numb+1, 2 ):
    print(i)
    
    