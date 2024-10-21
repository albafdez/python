"""Escribir un programa que pregunte al usuario por el número de horas trabajadas y el coste por hora. Después debe mostrar por pantalla la paga que le corresponde."""

hours=float(input("Hours worked? "))
salaryhour=float(input("How much you get paid per hour worked? "))
salary=hours*salaryhour

print("Your salary this month is", salary, "€")