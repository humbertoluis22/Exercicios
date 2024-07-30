print('Verificação de numero DECIMAL/INTEIRO\n')

numero_informado = float(input('Digite um numero para verificação : '))
validador = round(numero_informado)

if numero_informado == validador:
    print('Numero Inteiro !!')
else:
    print('Numero Decimal !!')