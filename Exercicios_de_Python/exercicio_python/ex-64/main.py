from medicos import *

print('******AGENDAMENTO DE CONSULTA**********\n')
while True:
    opcao = input('Deseja Agendar uma consulta [1-Sim | 2-Não] : ')[0]
    if not opcao.isnumeric():
        print('**************')
        print('Opção invalida')
        print('**************')
        continue
    elif opcao == '2':
        print('TCHAU TCHAU ')
        break
    else:
        print('\n***********Escolha um medico para consulta***********\n')
        for i in range(len(lista_medicos)):
            print(f'{i} - {lista_medicos[i]}')
        print()
        print('**********************')
        escolha_medico = int(input(f'escolha entre 0 e {len(lista_medicos) -1 }: '))
        print('**********************')
        print(f'Consulta Agendado com sucesso com o/a {lista_medicos[escolha_medico]}')
        print('**********************\n')

        
        