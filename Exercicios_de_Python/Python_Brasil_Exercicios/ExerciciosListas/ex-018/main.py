numeros_jogadores = []
pontos = []
jogadores = []
melhor_jogador = 0
maior = 0

while True:
    jogador = input("Informe o numero do seu voto [1-23] [0-sair] : ").strip()

    if jogador == "0":
        print("Tchau Tchau ! :D")
        break
    elif not jogador.isnumeric() or int(jogador) < 0 or int(jogador) > 23:
        print("Jogador invalido !!")
        continue

    numeros_jogadores.append(jogador)

for jogador in numeros_jogadores:
    if jogador in jogadores:
        continue
    ponto = numeros_jogadores.count(jogador)
    pontos.append(ponto)
    jogadores.append(jogador)

jogador_ponto = zip(jogadores, pontos)
print()

print("Resultado da votação:\n")
print(f"Foram computados {len(numeros_jogadores)} votos.\n")
print("JOGADOR     VOTOS            %")

soma_pontos = sum(pontos)
porcentagem = 0

for jogador, pontos in jogador_ponto:
    print(f"{jogador:<10}    {pontos:<10}  {((pontos / soma_pontos)*100):.1f} %")

    if pontos > maior:
        maior = pontos
        melhor_jogador = jogador
        porcentagem = (pontos / soma_pontos) * 100

print(
    f"O melhor jogar foi : {melhor_jogador} com {maior} pontos,"+ 
    f"correspondendo a {porcentagem:.1f}% do total de votos."
)
