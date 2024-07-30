nome = input('Digite seu nome: ')

for i in range(0,len(nome)+1):
    for y in range(0,i):
        print(nome[y],end='')
    print()