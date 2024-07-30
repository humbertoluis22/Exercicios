print("CANDIDATOS !!")
print(
    """
1 - Matheus
2 - Diogo
3 - Felipe
4 - Alex
5 - voto nulo
6 - voto em branco
\n"""
)

candidato_1 = candidato_2 = candidato_3 = candidato_4 = 0
voto_branco = voto_nulo = 0

eleitores = int(input("Informe a quantidade de eleitores: "))

for i in range(1, eleitores + 1):
    voto = int(
        input("Digite o valor do seu voto de acordo com a numeração da tabela : ")
    )
    if voto == 1:
        candidato_1 += 1
    elif voto == 2:
        candidato_2 += 1
    elif voto == 3:
        candidato_3 += 1
    elif voto == 4:
        candidato_4 += 1
    elif voto == 5:
        voto_nulo += 1
    elif voto == 6:
        voto_branco += 1


percentual_nulos = (voto_nulo / eleitores) * 100
percentual_branco = (voto_branco / eleitores) * 100

print(
    "\n**************************************************************************************"
)
print(f"A quantidade  de votos para o candidato 1 é {candidato_1}")
print(f"A quantidade  de votos para o candidato 2 é {candidato_2}")
print(f"A quantidade  de votos para o candidato 3 é {candidato_3}")
print(f"A quantidade  de votos para o candidato 4 é {candidato_4}")
print(f"Total de votos em branco é de {voto_branco}")
print(f"Total de votos em nulo é de {voto_nulo}")
print(
    f"A percentagem de votos nulos sobre o total de votos é de {percentual_nulos:.2f} % "
)
print(
    f"A percentagem de votos em branco sobre o total de votos é de {percentual_branco:.2f} % "
)
print(
    "**************************************************************************************"
)
