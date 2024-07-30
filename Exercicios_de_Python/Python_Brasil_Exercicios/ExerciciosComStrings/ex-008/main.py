palavra = input('Digite uma palavra : ').strip().lower()
nova_palavra = ''

for i in range(1,len(palavra)+1):
    nova_palavra  +=  palavra[-i]

if palavra == nova_palavra:
    print('A palavra é Palíndromo')
else:
    print('A palavra NÂO É Palíndromo' )

