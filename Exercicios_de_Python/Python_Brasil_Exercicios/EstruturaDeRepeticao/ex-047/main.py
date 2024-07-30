qtd_atletas = int(input('Informe a quantidade de atletas : '))

for i in range(1, qtd_atletas + 1): 
    ginasta = input('Informe o nome do ginasta : ').strip().capitalize()
    soma_pontos  = 0 
    maior = menor = 0
    print(f'\nAtleta : {ginasta}')
    for i in range(1,7+1):
        nota = float(input('Nota: '))
        if i == 1 :
            maior = menor =  nota
        if nota > maior:
            maior = nota
        elif nota < menor :
            menor = nota
        soma_pontos += nota
    
    media = ((soma_pontos - maior) - menor) / 5
    print('\nResultado final :')
    print(f'Atleta : {ginasta} ')
    print(f'Melhor nota : {maior}')
    print(f'Pior nota : {menor}')
    print(f'Média : {media}\n')