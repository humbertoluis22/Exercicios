turmas = int(input("Informe a quantidade de turmas : "))
soma_alunos = 0 
print()
for i in range(1, turmas + 1):
    qtd_alunos = -1 
    while True :
        qtd_alunos = int(input(f"Informe a quantidade de alunos da turma {i}: "))
        if qtd_alunos > 0 and qtd_alunos <= 40: 
            soma_alunos += qtd_alunos
            break
        else:
            print(f'\nQuantidade invalida para a turma {i} [1-40]\n')
    
media_alunos = soma_alunos / turmas
print(f'A media de alunos por turma é {round(media_alunos)}')