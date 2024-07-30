tabuada  = int(input('Montar a tabuada de: ')) 
comeco = int(input('Começar por: '))
fim = int(input('Terminar em: '))

while fim < comeco:
    print('\nO final precisa ser maior que o começo \n')
    comeco = int(input('Começar por: '))
    fim = int(input('Terminar em: '))
               
print(f'\nVou montar a tabuada de {tabuada} começando em {comeco} e terminando em {fim}:')

for i in range(comeco,fim+1):
    print(f'{i} X {tabuada} = {i * tabuada}')