print('Loja\n')

fruta_um = float(input('Digite  a quantidade em KG de morango : '))
fruta_dois = float(input('Digite  a quantidade em KG de maça : '))


if fruta_um <= 5:
    kg_morango = 2.50
elif fruta_um >=5 :
    kg_morango = 2.20

valor_compra_morango = kg_morango * fruta_um

if valor_compra_morango > 25 or fruta_um > 8:
    desconto_morango = valor_compra_morango * 0.1

if fruta_dois <= 5:
    kg_maca = 1.80
elif fruta_dois >= 5:
    kg_maca = 1.50

valor_compra_maca = kg_maca* fruta_dois
if valor_compra_maca > 20 or fruta_dois > 8:
    descontoo_maca = valor_compra_maca * 0.1


print(f'\nO valor dos morango ficou R$:{(valor_compra_morango - desconto_morango):.2f}')
print(f'Você recebeu R$:{desconto_morango:.2f} de desconto\n')
print(f'O valor das maças ficou R${(valor_compra_maca - descontoo_maca):.2f}')
print(f'Você recebeu R$:{descontoo_maca:.2f} de desconto\n')
