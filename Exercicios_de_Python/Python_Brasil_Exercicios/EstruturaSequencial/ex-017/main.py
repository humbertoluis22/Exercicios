
area = float(input('digite o tamanho da  area que deseja pintar : '))
mais_10 = area * 0.10
area += mais_10
qtd_litros = round(area / 6)
qtd_latas_necessaria = round(max(qtd_litros / 18,1))
qts_galoes = round(max(qtd_litros/3.6,1))


litros_restante_lata = round(qtd_litros % 18)
preencher_galoes = round(litros_restante_lata / 3.6)
print(preencher_galoes)

print()

print(f'Para pintar a area informada de {area}M² é necessario {qtd_latas_necessaria:.0f} latas' 
      +f' que custam R$:{qtd_latas_necessaria* 80.00:.2f}')

print(f'Para pintar a area informada de {area}M² é necessario {qts_galoes:.0f} galões' 
      +f' que custam R$:{qts_galoes* 25.00:.2f}')

print(f'Para pintar a area informada de {area}M² é necessario {qtd_latas_necessaria} latas e {preencher_galoes} galões '
      +f'Totalizando o valor de R$: {(qtd_latas_necessaria * 80.00 ) + (preencher_galoes * 25.00):.2f}')