
for i in range(1,5+1):
    numero = int(input(f'Informe o numero {i} : '))
    if i == 1:
        maior  = numero
    if numero > maior:
        maior = numero
print(f'o maior numero é {maior}')