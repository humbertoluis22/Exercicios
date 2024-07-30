n1 = int(input('Digite o primeiro numero : '))
n2 = int(input('Digite o segundo numero : '))
soma = 0

for i in range(n1 + 1,n2):
    soma += i 

print(f'A soma dos numeros é {soma}')