numero = int(input('Informe um numero : '))
contador = 0 

for i in range(2,numero + 1):
    if numero % i == 0 :
        contador +=1

if contador == 1:
    print(f'O numero {numero}  É PRIMO !!')
else: 
    print(f'O numero {numero} NÂO É PRIMO !!')