tamanho_arquivo = int(input("informe o tamanho do arquivo para dowload em MB: "))
velocidade_internet = int(
    input("informe a velocidade de um link de internet em Mbps: ")
)

tempo_segundo = round(tamanho_arquivo * 8) / (velocidade_internet)

print(
    f"Para baixar um arquivo de {tamanho_arquivo} MB ira levar {tempo_segundo:.2f} segundos"
)