"""Pedir el nombre de un producto por teclado y su peso (teniendo en cuenta que puede tener decimales).
Mostrar los datos por pantalla teniendo en cuenta que, si el peso introducido tiene más de 3 decimales, 
se requiere redondearlo exactamente a 2."""

nombre=input("Dame el nombre del producto: ")
peso=float(input("Dame el peso del producto: "))

print("Tu producto es %s y pesa %.2f"%(nombre,peso))