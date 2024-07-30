print('Conta espaços e vogais.\n')

letra_quantidade = []
valida_letra = []

palavra = input('Digite uma palavra: ')

for letra in (palavra):
    if letra  in valida_letra:
        continue
    valida_letra.append(letra)
    if letra.upper() in 'AEIOU' or letra == ' ':
        letra_quantidade.append([letra,palavra.count(letra)])

for letra,quantidade in letra_quantidade:
    if letra == ' ':
        print(f'Tem {quantidade} espaços na palavra')
    else:
        print(f'A letra {letra} apareceu {quantidade} vezes')
