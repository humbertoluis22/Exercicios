print('Caixa eletronico\n')

valor_saque = int(input('diite o valor do saque [10 - 600 ] : '))

if valor_saque < 10 or valor_saque > 600:
    print('Valor inválido')
else:
    nota_cem = valor_saque // 100
    nota_cinquenta =  (valor_saque % 100) // 50 
    nota_dez = ((valor_saque % 100) % 50) //10
    nota_cinco = (((valor_saque % 100) % 50) % 10) //5
    nota_um = ((((valor_saque % 100) % 50) % 10) % 5) // 1

    print(f'{nota_cem} notas de cem')
    print(f'{nota_cinquenta} notas de cinquenta')  
    print(f'{nota_dez} notas de dez ')
    print(f'{nota_cinco} notas de cinco')
    print(f'{nota_um} notas de um ')