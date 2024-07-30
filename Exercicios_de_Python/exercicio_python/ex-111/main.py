import random 

numero_aleatorio = random.randint(0,10)

chute = int(input('digite o seu chute: '))

if chute == numero_aleatorio:
    print('Parabens, vc acertou !!!!')
else:
    print(f'Que pena, vc errou. O numero correto era {numero_aleatorio}')