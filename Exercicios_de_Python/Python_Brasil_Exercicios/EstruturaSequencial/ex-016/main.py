
area = float(input('digite o tamanho da  area que deseja pintar : '))
qtd_litros = (area / 3)
qtd_latas_necessaria = round(max(qtd_litros / 18,1))

print(f'Para pintar a area informada de {area}M² é necessario {qtd_litros:.2f} litros ' 
      +f'que custa R$:{qtd_latas_necessaria* 80.00:.2f}')