eleitores = int(input("Infome a quantidade de eleitores : "))
candidato_1 = candidato_2 = candidato_3 = 0

for i in range(1,eleitores+1):
    voto = int(input(f'eleitor {i} [1 | 2 | 3] : '))
    if voto == 1 :
        candidato_1 +=1
    elif voto == 2:
        candidato_2 +=1
    elif voto == 3:
        candidato_3 += 1
    
print(f'\nCandidato 1 recebeu {candidato_1} votos')
print(f'Candidato 2 recebeu {candidato_2} votos')
print(f'Candidato 3 recebeu {candidato_3} votos\n')
