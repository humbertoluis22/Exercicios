print("Lojas Tabajara")

while True:
    qtd_produtos = int(input("Informe a quantidade de produtos :"))
    soma_valor = 0
    for i in range(1, qtd_produtos + 1):
        valor = float(input("Informe o valor do produto : "))
        soma_valor += valor

    print(f"\nO valor da compra foi de R$ : {soma_valor:.2f}")
    dinheiro = 0 
    while dinheiro < soma_valor:
        dinheiro = float(input("Dinheiro R$ : "))
    troco = dinheiro - soma_valor
    
    print(f"Troco R$ : {troco:.2f}\n ")
    
    opcao = ''
    while opcao != '0' or opcao != '1':
        opcao = input('0-sair | 1- fazer nova compra  : ')
        if  opcao not in '01':
            print('Opção invalida !!')
        if opcao == '1':
            break
        else:
            print('Tchau tchau !! :D')
            exit()

