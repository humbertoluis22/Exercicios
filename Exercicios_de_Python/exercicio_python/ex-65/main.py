from medicos import *
from cadastro import *
print('******AGENDAMENTO DE CONSULTA**********\n')
def agendar_consulta() ->None:
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

verificacao = input('você ja possui cadastro? [S/N] : ').upper()[0].strip()

if verificacao == 'N':
    novo_cadastro = input('deseja criar uma cadastro ? [S/N]').upper()[0].strip()
    if novo_cadastro == 'N':
        print('Não poderemos prosseguir com o agendamento, até logo !')
    elif novo_cadastro =='S':
        usuario = input('digite seu nome  : ')
        senha = input('digite a sua senha : ')
        novo_cadastro = {'usuario':usuario,'senha':senha}
        cadastro.update(novo_cadastro)
        print('\n***********usuario cadastrado com sucesso***********\n')
        agendar_consulta()

if verificacao =='S':
    senha_verificacao = input('digite a sua senha : ')
    usuario_verificacao = input('digite o seu usuario : ')
    if usuario_verificacao == cadastro['nome']:
        if senha_verificacao == cadastro['senha']:
           agendar_consulta()
        else:
            print('************senha invalida************')
    else:
        print('**********usuario não encontrado***********')




        
        