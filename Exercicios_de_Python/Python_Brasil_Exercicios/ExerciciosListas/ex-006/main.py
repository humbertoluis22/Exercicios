alunos_medias =[]

for i in range(1 , 11):
    numero = int(input('Digite o numero do aluno : '))
    soma_nota = 0 
    for y in range(1,5):
        nota = float(input(f'Digite a nota {y} do aluno {numero}: '))
        soma_nota += nota
    media = soma_nota /4 
    aluno_media = [numero,media]
    alunos_medias.append(aluno_media)


aluno_sete = []  
print('\n********************')
print(alunos_medias)
print('********************\n')
for al_media in alunos_medias:
    if al_media[1] >=7 :
        aluno_sete.append(al_media[0])

print(f'Alunos  com media 7 + : {' , '.join([str(aluno) for aluno in aluno_sete])} \n')

