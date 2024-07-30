from info_alunos import * 

soma_altura = 0
contador = 0

for altura in alturas:
    soma_altura += altura

media_altura = soma_altura / len(alturas)

idade_altura = zip(idades, alturas)

for alunos in idade_altura:
    if alunos[0] > 13 and alunos[1] < media_altura:
        contador += 1

print(f"Existem {contador} alunos com mais de 13 anos e com a altura a baixo da media")
