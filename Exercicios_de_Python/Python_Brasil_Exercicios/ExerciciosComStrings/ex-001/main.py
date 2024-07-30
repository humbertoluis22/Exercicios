primeira_palavra = input('Digite a primeira palavra ou frase: ')
segunda_palavra = input('Digite a segunda palavra ou frase: ')
print()
print(f'string 1 : {primeira_palavra}')
print(f'string 2 : {segunda_palavra}')
print(f'Tamanho de "{primeira_palavra}" : {len(primeira_palavra)}')
print(f'Tamanho de "{segunda_palavra}" : {len(segunda_palavra)}')
print(f'As duas string sao de tamanhos ' +
      f'{('iguais' if len(primeira_palavra) == len(segunda_palavra)else 'diferentes')}')
print(f'As duas string possuem conteudo ' 
      f'{('iguais' if primeira_palavra.strip() == segunda_palavra.strip() else 'diferentes')}')
