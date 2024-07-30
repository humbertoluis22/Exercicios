from bomba_compustivel import BombaDeCompustivel

bomba_1 = BombaDeCompustivel('Gasolina',5.90,300)
print(bomba_1)
bomba_1.abastecer_por_litro(18)
print(bomba_1)
bomba_1.abastecer_por_valor(29.40)
print(bomba_1)
bomba_1.alterar_combustivel('etanol')
bomba_1.alterar_valor(4.60)
print(bomba_1)
