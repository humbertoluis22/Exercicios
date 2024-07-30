print("Coleção de CDs\n")
qtd_cds = int(input("Informe a quantidade de CDs: "))
soma_valores = 0

for i in range(1, qtd_cds + 1):
    valor = float(input(f'Informe o valor pago no CD {i}: '))
    soma_valores += valor

media = soma_valores / qtd_cds
print(f'\nO valor medio gasto por cd é R$:{media:.2F}\n')