numero = int(input('digite um numero: '))
quantidade = 0 

for i in range(2,numero+1):
    if numero % i == 0:
        quantidade +=1

if quantidade == 1:
    print(f'O numero {numero} é primo')
else:
    print(f'o numero {numero} NÃO é primo')
    print(f'é dividido {quantidade+1} vezes')