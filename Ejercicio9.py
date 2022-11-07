palabra = input("Introduce una palabra\n")
vocales = ['a', 'e', 'i','o','u']

for vocal in vocales:
    tiempo = 0
    for letra in palabra:
        if letra == vocal:
            tiempo += 1
        print("La vocal" + vocal + "aparece" + str(tiempo) + "veces")






