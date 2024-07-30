soma = 0 
for i in range(1,5+1):
    numero = int(input(f'Digite o numero {i}: '))
    soma += numero

media = soma / 5

print(f'A  soma dos numeros é {soma}')
print(f'A media dos numeros é {media}')
