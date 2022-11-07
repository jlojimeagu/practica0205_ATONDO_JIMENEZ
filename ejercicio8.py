# Escribir un programa que pida al usuario
# una palabra y muestre por pantalla si
# es un palíndromo.
palabra = input('indica la palabra:\n')
reverso = palabra
palabra = list(palabra)
reverso = list(reverso)
reverso.reverse()
if palabra == reverso:
    print('se lee tanto al derecho como al reves(palindromo)', 'palabra al derecho',
          ''.join(palabra), '\n',
          'palabra al reves',
          "".join(reverso))
else:
    print('no es una palabra palindroma')
