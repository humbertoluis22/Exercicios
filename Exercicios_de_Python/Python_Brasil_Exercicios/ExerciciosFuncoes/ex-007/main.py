def valorPagamento (valor:float,dias_atraso:int) -> float:
    multa_atraso = 0.03
    juros_dia = 0.01
    valor_juros = (valor*juros_dia) * dias_atraso

    valor = (valor*multa_atraso) + valor_juros + valor
    return valor

def  executa_programa()-> None:
    valores_pagos = []
    while True:
        valor_despesa = float(input('Informe o valor da despesa [0-sair] : '))

        if valor_despesa == 0:
            print('TCHAU TCHAU :p')
            break

        dias_atraso = int(input('Informe os dias em atraso : '))
        pagar_valor = valorPagamento(valor_despesa,dias_atraso)
        valores_pagos.append(pagar_valor)
        print(F'\nO  Valor a ser pago sera R$: {pagar_valor:.2f} !!')
        print()
    
    print('\nRELATORIO\n')
    print(f'Quantidade de despesas do dia :  {len(valores_pagos)}')
    print(f'valor total pago : R$:{(sum(valores_pagos)):.2f}\n' )

executa_programa()