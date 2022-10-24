asignatura = ["Matematicas", "Fisica", "Quimica",
                       "Historia", "Lengua"]
nota = []

for materia in asignatura:
    print("Introduce la nota", materia)
    nota.append(input())

for id in range(len(asignatura)):
    print(asignatura[id], "=", nota[id])



