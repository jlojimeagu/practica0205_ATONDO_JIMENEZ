A = ((1, 2, 3),
     (4, 5, 6))
B = ((-1, 0),
     (0, 1),
     (1, 1))
resultado = [[0, 0],
             [0, 0]]
for a in range(len(A)):
    for b in range(len(B[0])):
        for num in range(len(B)):
            resultado[a][b] += A[a][num] * B[num][b]

for a in range(len(resultado)):
    resultado[a] = tuple(resultado[a])

resultado = tuple(resultado)

for a in range(len(resultado)):
    print(resultado[a])
