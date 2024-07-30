def boas_vindas(nome:str,sobrenome:str) -> str:
    return f'Boas Vindas {nome} {sobrenome}!!!'

nome = input('digite seu nome: ')
sobrenome = input('digite seu sobrenome: ')

mensagem = boas_vindas(nome,sobrenome)
print(mensagem)
