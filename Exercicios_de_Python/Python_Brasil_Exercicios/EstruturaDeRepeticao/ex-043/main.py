soma_valor = 0 

while True:
    print('CARDAPIO !!')
    print('''
    Cachorro Quente 100     R$ 1,20
    Bauru Simples   101     R$ 1,30
    Bauru com ovo   102     R$ 1,50
    Hambúrguer      103     R$ 1,20
    Cheeseburguer   104     R$ 1,30
    Refrigerante    105     R$ 1,00
    \n''')

    codigo = int(input('Informe o codigo do produto : '))
    qtd_produto = int(input('informe a quantidade de itens : '))

    if codigo == 100:
        valor = 1.20
        soma_valor += valor * qtd_produto
    elif codigo == 101:   
        valor = 1.30
        soma_valor += valor * qtd_produto
    elif codigo == 102:
        valor = 1.50
        soma_valor += valor * qtd_produto
    elif codigo == 103:
        valor = 1.20
        soma_valor += valor * qtd_produto
    elif codigo ==104:
        valor = 1.30
        soma_valor += valor * qtd_produto
    elif codigo == 105:
        valor = 1.00
        soma_valor += valor * qtd_produto

    print('\nDeseja efetuar mais algum pedido ? ')
    opcao = int(input('[1-sim | 2-não]'))
    if opcao == 2 :
        break

print(f'\nValor final a ser pago R$ : {soma_valor:.2f}\n')