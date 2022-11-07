A = ((1, 2, 3),
     (4, 5, 6))
B = ((-1, 0),
     (1, 1))
resultado = [[0, 0],
             [0, 0]]
for A in range(len(A)):
    for B in range(len(B[0])):
        for num in range(len(B)):
            resultado[A][B] += A[A][num] * B[num][B]

for A in range(len(resultado)):
    resultado[A] = tuple(resultado[A])

resultado = tuple(resultado)

for A in range(len(resultado)):
    print(resultado[A])

