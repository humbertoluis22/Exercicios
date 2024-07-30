numeros = int(input('Informe a quantidade de numeros : '))

for i in range(1, numeros + 1):
    n = -1 
    while  n < 0 or n > 1000:
        n = int(input(f'Infome o numero {i} [0-1000]: '))
    if i == 1 :
        maior = menor = n 
    if maior < n :
        maior = n
    if menor > n :
        menor  = n 

print(f'O maior numero informado foi : {maior}')
print(f'O menor numero informado foi : {menor}')