nome = input('Digite o seu nome : ')
novo_nome = ''

for i in range(1,len(nome)+1):
    novo_nome += nome[-i].upper()

print(f'O nome {nome} ao contrario e em maisculo fica : {novo_nome}')