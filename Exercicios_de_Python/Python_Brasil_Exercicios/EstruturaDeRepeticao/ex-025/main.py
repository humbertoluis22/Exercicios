pessoas = int(input("Informe a quantidade de pessoas : "))
soma_idade = 0

for i in range(1, pessoas + 1):
    idade = int(input(f"informe a idade da pessoa numero {i}: "))
    soma_idade += idade

media_idade = soma_idade / pessoas
if media_idade > 0 and media_idade <= 25:
    print('Turma Jovem')
elif media_idade >= 26 and media_idade <= 60:
    print('Turma Adulta')
else:
    print('Turma idosa') 