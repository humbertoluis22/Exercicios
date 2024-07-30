numeros= []
for numero in range(2000,2200 + 1 ): 
    if numero % 7  == 0 and numero % 5 != 0:
        numeros.append(str(numero))

print(','.join(numeros))

