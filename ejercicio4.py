n_ganadoresloteria = []
for numero in range(6):
    n_ganadoresloteria.append(int(input("dime los numeros de loteria, pon uno por uno!!!:\n")))
n_ganadoresloteria.sort()
print("los ganadores son:", n_ganadoresloteria)