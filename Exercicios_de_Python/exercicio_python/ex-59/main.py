def monta_mensagem(nome:str, idade:int = 18, cargo = 'Operador') ->str:
    return f'Nome do Funcionario : {nome} | Idade:{idade} | Função: {cargo}'
nome = input('digite seu nome: ')
mensagem = monta_mensagem(nome,cargo='DEV')
print(mensagem)