print('Realizando Operacação desejada !!\n')

numero_um = float(input('Digite o primeiro numero: '))
numero_dois = float(input('Digite o segundo numero: '))

print('Informe a operação desejada')
opcao = int(input('1-par ou impar | 2 - positivo ou negativo | '
                  +'3 - inteiro ou decimal: '))


if str(opcao) not in '123':
    print('OPÇÃO INVALIDA !!')

if opcao == 1:
    if numero_um % 2 == 0 :
        print(f'O numero {numero_um} é Par')
    elif numero_um % 2 != 0 :
        print(f'O numero {numero_um} é Impar')
    if numero_dois % 2 == 0 :
        print(f'O numero {numero_dois} é Par')
    elif numero_dois % 2 != 0 :
        print(f'O numero {numero_dois} é Impar')

elif opcao == 2:
    if numero_um < 0 :
        print(f'O numero {numero_um} é negativo')
    elif numero_um > 0 :
        print(f'O numero {numero_um} é positivo')
    if numero_dois < 0 :
        print(f'O numero {numero_dois} é negativo')
    elif numero_dois > 0 :
        print(f'O numero {numero_dois} é positivo')

elif opcao == 3 :
    validador_um = round(numero_um)
    validador_dois = round(numero_dois)
    if numero_um == validador_um : 
        print(f'O numero {numero_um} é inteiro')
    elif numero_um != validador_um:
        print(f'O numero {numero_um} é decimal')
    if numero_dois == validador_dois : 
        print(f'O numero {numero_dois} é inteiro')
    elif numero_dois != validador_dois:
        print(f'O numero {numero_dois} é decimal')