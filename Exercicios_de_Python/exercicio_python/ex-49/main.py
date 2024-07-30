print("*** CADASTRO DE NOTAS DE ALUNO ***")

alunos:list[str] = []
notas:list[list] = []

while True:
    opcao = input('Deseja Cadastrar um novo Aluno com Três notas? [S/N] : ').upper()[0]
    if not opcao.isnumeric() and opcao not in ['N','S']:
        print('Opção invalida !!')
        continue
    if opcao == 'N':
        print('\nTchau Tchau :D\n')
        break
    if opcao == 'S':
        nome = input('Digite o nome do aluno: ')
        alunos.append(nome)
        notas_semestre = []
        for i in range(1,3+1):
            nota = int(input(f'digite a {i} nota: '))
            notas_semestre.append(nota)
        notas.append(notas_semestre)

media = [round(sum(nota)/len(nota)) for nota in notas]
aluno_media = list(zip(alunos,media))
for aluno,media in aluno_media:
    print(f'O/A aluno {aluno} ficou com a media de {media} !!')
