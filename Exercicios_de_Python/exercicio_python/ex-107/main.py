from array import * 

lista = array('i',[i for i in range(5)])
lista2 = array('i')
for numero in lista:
    print(numero)
    if numero % 2 ==0:
        lista2.append(numero)

for numero in lista2:
    print(f'Numero par: {numero}')