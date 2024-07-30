palavra_frase = input('digite uma palavra ou frase: ').upper().strip().replace(' ','')
comparacao = ''

for i in range(len(palavra_frase)+1):
    if i == 0:
        continue
    comparacao += palavra_frase[-i]

if palavra_frase == comparacao:
    print('A palavra é um palíndromo')
else:
    print('A palavra NÂO é um palíndromo')