from alfabeto import * 

print('Leet spek generator\n')
palavra = input(
    'Digite a palavra para a alteração : '
    ).strip().upper()

nova_palavra = ''
for letra in palavra:
    nova_palavra += leet_speak_dict[letra]

print(f'A palavra : {palavra} em Leet spek fica => {nova_palavra}\n')
