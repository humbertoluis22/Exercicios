def exibi_mensagem()->None:
    global mensagem
    mensagem = 'aqui é uma mensagem ...'
    print(mensagem)


exibi_mensagem()
mensagem = 'aqui é outra mensagem'
print(mensagem)