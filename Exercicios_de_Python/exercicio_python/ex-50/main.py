print("*** PERGUNTAS E RESPOSTAS ***\n")
perguntas = ['Qual a capital do Brasil?',
             'Qual a capital da australia ?',
             'Qual o valor do PI com duas casa decimais? ',
             'Em qual cidade o PAPA mora? ']
gabarito = ['Brasilia','Canberra','3.14','Roma']


for i in range(len(perguntas)):
    print(perguntas[i])
    print('======================')
    resposta = input('digite a resposta: ').upper().strip()
    if resposta == gabarito[i].upper().strip():
        print('Parabens você acertou !!\n')
    else:
        print(f'Resposta errada, a resposta correta é {gabarito[i]}\n')


