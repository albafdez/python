"""Escribir un programa que pida un número entero y escriba por pantalla:

- “El número introducido es PAR”, en el caso de que sea par.
- “El número introducido es IMPAR”, en el caso de que sea impar."""

# Pedir un número entero al usuario
number = int(input("Introduce un número entero: "))

# Verificar si el número es par o impar
if number % 2 == 0:
    print("El número introducido es PAR")
else:
    print("El número introducido es IMPAR")
