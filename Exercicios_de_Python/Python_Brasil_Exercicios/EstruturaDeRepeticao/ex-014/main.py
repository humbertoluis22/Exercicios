pares = 0 
impares = 0 

for i in range(1,10 +1):
    numero = int(input(f'Digite o numero {i}: '))
    if numero % 2 == 0 :
        pares += 1
    else:
        impares += 1

print(f'\nQuantidade de numero pares : {pares}')
print(f'Quantidade de numero impares : {impares}')