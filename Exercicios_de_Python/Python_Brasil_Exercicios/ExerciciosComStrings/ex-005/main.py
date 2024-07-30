nome = input('Digite um  nome: ')

for i in range(0,len(nome)+1):
    if  i == 0:
        print(nome)
    else:
        print(nome[:-i])
