soma = 0 
quantidade_impares = 0

for  i in range(0,100+1):
    if i % 2 != 0: 
        print(i)
        soma += i 
        quantidade_impares += 1

print()
print(f'A soma dos numeros é {soma}')
print(f'A quantidade de numeros impares é {quantidade_impares}')