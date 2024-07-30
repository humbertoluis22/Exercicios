lista = [i for i in range(0,501)]
lista2= []

for numero in lista:
    if numero % 7 == 0 and numero %5 ==0:
        lista2.append(numero)
    
print(lista2)
