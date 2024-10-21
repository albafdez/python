#Generar un número aleatorio entre 1 y 20. Luego informar si el número tiene uno o dos dígitos

import random

# Generar un número aleatorio entre 1 y 20
random_number = random.randint(1, 20)

# Verificar si el número tiene uno o dos dígitos
if random_number < 10:
    print(f"El número generado es {random_number} y tiene un dígito.")
else:
    print(f"El número generado es {random_number} y tiene dos dígitos.")