num1 = float(input('Digite o primeiro numero : '))
num2 = float(input('Digite o segundo numero : '))
num3 = float(input('Digite o terceiro numero : '))

if num1 > num2 and num1 > num3:
    maior = num1
elif num2 > num1 and num2 > num3:
    maior = num2
elif num3 > num1 and num3 > num2:
    maior = num3

if num1 < num2 and num1 < num3:
    menor = num1
elif num2 < num1 and num2 < num3:
    menor = num2
elif num3 < num1 and num3 < num2:
    menor = num3

else:
    print('numeros iguais')
    exit()

print(f'O maior numero é {maior}')
print(f'O menor numero é {menor}')