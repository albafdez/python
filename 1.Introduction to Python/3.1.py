"""Realizar un programa en Python que imprima por pantalla los datos que se le han pedido por teclado: Nombre, Apellidos ,Edad, DNI y Domicilio"""

nombre=input("Nombre: ")
apellido=input("Apellido: ")
edad=int(input("Edad: "))
dni=input("DNI: ")
domicilio=input("Domicilio: ")

print("Los datos dados son: %s, %s, %d, %s, %s"%(nombre,apellido,edad,dni,domicilio))