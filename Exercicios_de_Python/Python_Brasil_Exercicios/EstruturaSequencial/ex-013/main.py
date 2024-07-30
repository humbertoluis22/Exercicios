altura = float(input('Digite a sua altura: '))

peso_masculino = (72.7*altura) - 58
peso_feminino = (62.1*altura) - 44.7

print(f'Peso ideal para homens é {peso_masculino:.2f} KG')
print(f'Peso ideal para mulheres é {peso_feminino:.2f} KG')