"""Escribir un programa que pida dos valores enteros y que imprima por pantalla:

- Si el primero es menor que el segundo, que imprima el mensaje “Primero menor”.
- Si el segundo es menor que el primero, que imprima el mensaje “Segundo menor”.
- Si los números son iguales, que imprima el mensaje “Son iguales”."""

# Pedir dos valores enteros al usuario
first_number = int(input("Introduce el primer número entero: "))
second_number = int(input("Introduce el segundo número entero: "))

# Comparar los números e imprimir el mensaje correspondiente
if first_number < second_number:
    print("Primero menor")
elif second_number < first_number:
    print("Segundo menor")
else:
    print("Son iguales")