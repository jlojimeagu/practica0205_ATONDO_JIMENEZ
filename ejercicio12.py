lista_num = input("dime los numeros separados por una coma ( , ):\n")
lista_num = lista_num.split(',')
lista = len(lista_num)
for num in range(lista):
    lista_num[num] = int(lista_num[num])
sample = tuple(lista_num)
suma = 0
suma_des = 0
for num in sample:
    suma += num
    suma_des += num**2
media = suma/lista
desv = (suma_des/lista-media**2)**(1/2)
print('La media es', media, ', y la desviación típica es', desv)