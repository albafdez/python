"""Crear un comparador de años. Se debe pedir el año actual y, después, un año que aleatorio. Una vez introducidos estos datos, deben aparecer los siguientes mensajes:

- Desde el año xxx han pasado yyy años.
- Para llegar al año xxxx faltan yyy años.
- xxx es la fecha que has puesto en segundo lugar (la que te apetecía).
- yyy es la resta entre las dos fechas.
- Los mensajes aparecerán según si la segunda fecha es mayor o menor a la actual."""

# Pedir el año actual y un año aleatorio
current_year = int(input("Introduce el año actual: "))
random_year = int(input("Introduce el año que te apetezca: "))

# Calcular la diferencia entre los años
difference = abs(current_year - random_year)

# Mostrar la diferencia en años
print(f"La diferencia entre {current_year} y {random_year} es de {difference} años.")