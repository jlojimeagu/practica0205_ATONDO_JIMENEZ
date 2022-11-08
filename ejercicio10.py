# Escribir un programa que almacene en una lista
# los siguientes precios, 50, 75, 46, 22, 80, 65, 8,
# y muestre por pantalla el menor y
# el mayor de los precios.
precios = [50, 75, 46, 22, 80, 65, 8]
min = max = precios[0]
for price in precios:
    if price < min:
        min = price
    elif price > max:
        max = price
print("El mínimo precio es" + str(min))
print("El máximo precio es" + str(max))
