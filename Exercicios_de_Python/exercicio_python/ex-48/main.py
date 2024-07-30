print('***CADASTRO***')
nome = input('Digite a seu nome: ')
idade = int(input('Digite a sua idade'))
sexo = input('Informe o seu sexo [M/F] :  ').upper()
sexo = sexo[0]
estado_civil = input('Informe seu estado civil: ')
nacionalidade = input('Informe sua nacionalidade: ')
faixa_de_renda = float(input('Informe sua faixa de renda: '))

cadastro = {'nome':nome , 'idade': idade, 'sexo': sexo, 'estado civil':estado_civil,'nacionalidade':nacionalidade,
            'faixa de renda':faixa_de_renda
            }
print(f'''
*** INFORMAÇÕES DO CADASTRO***
NOME = {cadastro['nome']}
IDADE = {cadastro['idade']}
SEXO = {cadastro['sexo']}
ESTADO CIVIL = {cadastro['estado civil']}
NACIONALIDADE = {cadastro['nacionalidade']}
FAIXA DE RENDA = {cadastro['faixa de renda']}
''')