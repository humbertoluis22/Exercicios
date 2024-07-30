numero = int(input('Digite um numero inteiro : '))
cont = 0 

for i in range(2,numero + 1):
    if numero % i ==0 :
        cont +=1

if cont != 1:
    print('O numero NÃO É PRIMO')    
else:
    print('O numero é PRIMO')