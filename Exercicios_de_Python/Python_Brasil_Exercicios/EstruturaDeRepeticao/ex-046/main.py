maior = menor = 0
soma_saltos = 0
atleta = "condicao"

ordem_extenso = {
    1: "Primeiro",
    2: "Segundo",
    3: "Terceiro",
    4: "Quarto",
    5: "Quinto"
}

while True:
    atleta = input("Informe o nome do atleta : ").capitalize().strip()
    if len(atleta) == 0:
        print('TCHAU TCHAU :D')
        break
    print(f'Atleta : {atleta}\n')
    for i in range(1, 5 + 1):
        salto = float(input(f"{ordem_extenso[i]} salto : "))
        soma_saltos += salto
        if i == 1:
            maior = menor = salto
        if salto > maior :
            maior = salto
        elif salto < menor :
            menor  = salto

    saltos_filtrados = (soma_saltos - maior) - menor
    media_saltos  = saltos_filtrados /3 

    print(f'\nMelhor salto:{maior} m ')
    print(f'Pior salto : {menor} m')
    print(f'Média dos demais saltos: {media_saltos:.2f}\n')
    print(f'Resultado Final : ') 
    print(f'{atleta} : {media_saltos:.2f} m\n')            