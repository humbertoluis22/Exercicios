numero = 0 
cont_25 = cont_50 = cont_75 = cont_100 = 0 

while numero >= 0 :
    numero = int(input('Informe um numero : ')) 
    if numero >= 0 and numero <= 25:
        cont_25 += 1
    elif numero >= 26 and numero <=50:
        cont_50 += 1
    elif numero >= 51 and numero <= 75 :
        cont_75 += 1 
    elif numero >= 76 and numero <= 100:
        cont_100 += 1 

print(f'No intevalo de  [0-25] existem {cont_25} numeros')
print(f'No intevalo de  [26-50] existem {cont_50} numeros')
print(f'No intevalo de  [51-75] existem {cont_75} numeros')
print(f'No intevalo de  [76-100] existem {cont_100} numeros')