carrinho_compras =[]

carrinho_compras.append(('banana',5.70))
carrinho_compras.append(('maça',4.5))
carrinho_compras.append(('pasta de amendoim',18.0))
carrinho_compras.append(('arroz',23))
carrinho_compras.append(('feijao',15.0))

total = 0 
for produto in carrinho_compras:
    total += produto[1]

print(f'o valor total do carrinho foi de {total}')