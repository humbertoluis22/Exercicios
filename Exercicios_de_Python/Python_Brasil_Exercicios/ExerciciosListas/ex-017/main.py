informacoes_atleta = []


while True: 
    informacoes_atleta_ = []
    saltos  = []
    atleta = input('Informe o nome do atleta : ').capitalize().strip()
    if len(atleta) == 0 :
        break
    
    for i in range(1,6):
        salto = float(input('Salto : '))
        saltos.append(salto)

    saltos_calc = saltos.copy()
    saltos_calc.pop(-1)
    saltos_calc.pop(0)
    media = sum(saltos_calc)/len(saltos_calc) 

    informacoes_atleta_.append(atleta)
    informacoes_atleta_.append(saltos)
    informacoes_atleta_.append(media)

    informacoes_atleta.append(informacoes_atleta_)


for nome,saltos,media in informacoes_atleta:
    print('\n*************************************************************')
    print(f"""
Atleta: {nome}
 
Primeiro Salto: {saltos[0]} m
Segundo Salto: {saltos[1]} m
Terceiro Salto: {saltos[2]} m
Quarto Salto: {saltos[3]} m
Quinto Salto: {saltos[4]} m

Resultado final:
Atleta: {nome}
Saltos: {' - '.join([str(salto) for salto in saltos])}
Média dos saltos:{media:.2f} m   
    """)
    print('*************************************************************')