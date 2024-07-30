import random


def craps() -> None:
    pontuacao_atual = 0
    cont = 0
    while True:
        dado_1 = random.randint(1, 6)
        dado_2 = random.randint(1, 6)
        cont += 1
        soma_ponto = dado_1 + dado_2

        if all([cont == 1, soma_ponto == 7 or soma_ponto == 11]):
            print("NATURAL !!")
            print("Parabens vc ganhou !!!!")
            break
        elif all([cont == 1, str(soma_ponto) in "23" or soma_ponto == 12]):
            print("CRAPS")
            print("Você perdeu !!!")
            break
        elif cont == 1 and str(soma_ponto) in "45689" or soma_ponto == 10:
            print("ponto !!")
            pontuacao_atual = soma_ponto
        elif pontuacao_atual == soma_ponto:
            print("Parabens Você ganhou !!")
            print("Fez o mesmo ponto novamente !!")
            break
        elif cont != 1 and soma_ponto == 7:
            print("Você perdeu, tirou 7 depois da primeira jogada")
            break


craps()
