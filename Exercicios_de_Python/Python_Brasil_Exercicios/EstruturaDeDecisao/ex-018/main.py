print('Validando se uma data é valida com base na formatação BR\n')

data_informada = input('Informe uma data no modelo dd/mm/aaaa : ')

data_verificacao  = data_informada.split('/')

if all([
    len(data_verificacao[0]) == 2,
    len(data_verificacao[1]) == 2,
    len(data_verificacao[2]) ==4,
    int(data_verificacao[0]) >= 1 and
    int(data_verificacao[0]) <= 12,
    int(data_verificacao[1]) >= 1 and
    int(data_verificacao[1]) <= 12
    ]
    ):
    print('Data valida')
else:
    print('Data invaldia')
