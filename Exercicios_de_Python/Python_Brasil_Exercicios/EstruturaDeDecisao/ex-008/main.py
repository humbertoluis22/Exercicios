produto1= float(input('Digite o valor do abacaxi: '))
produto2=float(input('Digite o valor do morango: '))
produto3= float(input('Digite o valor da melancia: '))

if produto1 < produto2 and produto1 < produto3:
    print(f'A escolha do produto para ser comprado é o abacaxi que custa: R$: {produto1:.2f}')
elif produto2 < produto1 and produto2 < produto3:
    print(f'A escolha do produtor para ser comprado é o morango que custa: R$: {produto2:.2f}')
elif produto3 < produto2 and produto3 < produto1:
    print(f'A escolha do produtor para ser comprado é a melancia que custa: R$: {produto3:.2f}')