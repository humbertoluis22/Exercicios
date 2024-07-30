num1 = float(input('Digite o primeiro numero : '))
num2 = float(input('Digite o segundo numero : '))
num3 = float(input('Digite o terceiro numero : '))

if num1 > num2 and num1 > num3:
    print(f'o maior numero é {num1}')
elif num2 > num1 and num2 >num3:
    print(f'o maior numero é {num2}')
elif num3 > num1 and num3 >num2:
    print(f'o maior numero é {num3}')
else:
    print('Numero iguais')