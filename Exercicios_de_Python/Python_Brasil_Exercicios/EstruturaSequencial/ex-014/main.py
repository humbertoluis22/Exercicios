peso  = float(input('Digite o peso total dos  peixes : '))
excesso = peso - 50 
excesso = max(excesso,0)
multa = excesso * 4
print(f'\nO valor da multa a ser pago por conta do excesso é R$:{multa:.2f}')