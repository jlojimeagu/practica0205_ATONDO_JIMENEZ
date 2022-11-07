# Escribir un programa que almacene las asignaturas de un curso
# (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado
# en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla
# las asignaturas que el usuario tiene que repetir.
lista_materia = ['matematicas', 'Física', 'Química', 'Historia', 'Lengua']
lista_nota = []
for materia in lista_materia:
    nota = float(input("tu nota en" + " " + materia + "\n"))
    if nota >= 5:
        lista_nota.append(materia)
for clase in lista_nota:
    lista_materia.remove(clase)
print('recupera:', 'y'.join(lista_materia))