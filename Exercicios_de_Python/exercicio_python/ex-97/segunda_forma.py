from operator import itemgetter

nome_nota = []

while True:
    informacoes = input('digite seu nome e duas notas separados por virgula: ')
    if not informacoes:
        break
    nome_nota.append(tuple(informacoes.split(',')))

print(sorted(nome_nota,key= itemgetter(0,1,2)))