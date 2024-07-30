from tamagushi import Tamagushi

bichinhos = []
while True:
    print("""
1 - criar um novo Tamagushi
2 - Alimentar os bichinhos
3 - Brincar com os bichinhos
4 - verificar informações do bicinhos
5 - sair
    """)
    opcoes = input('Informe a opcão : ')
    if not opcoes.isalnum():
        print('Opção invalida !!')
        continue
    elif opcoes == '1':
        nome = input('Informe o nome do tamagoshi: ')
        fome = float(input('Informe o nivel da fome: '))
        saude = float(input('Informe o nivel de saude: '))
        idade = int(input('Informe a idade : '))
        bichinho = Tamagushi(nome,fome,saude,idade)
        bichinhos.append(bichinho)
    elif opcoes == '2':
        fome = int(input('Informe a quantidade de alimento: '))
        for bichinho in bichinhos:
            bichinho.alimentar(fome)
    elif opcoes == '3':
        tempo = int(input('Informe a quantidade de minutos brincados: '))
        for bichinho in bichinhos:
            bichinho.brincar(tempo)
    elif opcoes == '4':
        for bichinho in bichinhos:
            print(bichinho)
    elif opcoes == '5':
        print('Tchau Tchau :P')
        break