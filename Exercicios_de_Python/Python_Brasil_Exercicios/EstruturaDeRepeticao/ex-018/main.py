numeros = int(input('Informe a quantidade de numeros : '))

for i in range(1, numeros + 1):
    n = int(input(f'Infome o numero {i}: '))
    if i == 1 :
        maior = menor = n 
    if maior < n :
        maior = n
    if menor > n :
        menor  = n 

print(f'O maior numero informado foi : {maior}')
print(f'O menor numero informado foi : {menor}')