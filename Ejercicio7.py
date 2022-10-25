abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                   'k', 'l', 'm', 'n', 'ñ', 'o', 'p', 'r', 's', 't', 'v', 'w', 'z']

for letra in range(len(abecedario), 1, -1):

    if letra % 3 == 0:
        abecedario.pop(letra-1)

print(abecedario)

