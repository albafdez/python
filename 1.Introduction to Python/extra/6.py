"""Escribir un programa que lea un entero positivo, 
, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta 
. La suma de los 
 primeros enteros positivos puede ser calculada de la siguiente forma:"""

n=int(input("Give me a postive number: "))

suma=(n*(n+1))/2
print("The sum of the first integer numbers from 1 to " + str(n) + " is " + str(suma))