numero = int(input('digite um numero : '))
soma = 0 
for i in range(1,numero):
    if numero % i == 0 :
        soma += i
if soma == numero:
    print('numero perfeito')
else:
    print(f'O numero {numero} não é perfeito')