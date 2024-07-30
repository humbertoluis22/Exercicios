votos = []
votos_verificacao = []
sistema_voto = []
total_votos = 0
maior = 0
indice = 0
sistema_operacional = [
    "",
    "Windows Server",
    "Unix",
    "Linux",
    "Netware",
    "Mac OS",
    "Outro",
]

print("Qual o melhor Sistema Operacional para uso em servidores?")
print(
    """
1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outros
"""
)

while True:
    voto = input("Informe seu voto [1-6] [0-sair] : ")
    if not voto.isnumeric() or int(voto) < 0 or int(voto) > 6:
        print("Opção inválida !!")
        continue
    elif voto == "0":
        print("TCHAU TCHAU :P\n")
        break
    total_votos += 1
    votos.append(voto)


for voto in votos:
    if voto in votos_verificacao:
        continue
    votos_verificacao.append(voto)
    qtd_votos = votos.count(voto)
    if qtd_votos > maior:
        maior = qtd_votos
        indice = int(voto)
    sistema_voto.append([sistema_operacional[int(voto)], qtd_votos])


print("Sistema Operacional     Votos   %")
print("-------------------     -----   ---")

for sistema, qtd_votos in sistema_voto:
    print(f"{sistema:<24} {qtd_votos:<6} {((qtd_votos / total_votos) * 100):.1f}%")
print("-------------------     -----")
print(f"Total                    {total_votos}")
print(
    f"\nO sistema operacional mais votado foi o {sistema_operacional[indice]}"
    + f" com {maior} votos correspondendo a {((maior/total_votos) * 100):.1f}% dos votos"
)
