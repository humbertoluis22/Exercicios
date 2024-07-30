perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

positivas = 0 

print('interrogatorio\n')

for pergunta in perguntas: 
    print(pergunta)
    opcao = input('1 - sim | 2 - não : ')
    if opcao == '1':
        positivas += 1

print()
if positivas  == 2:
    print('Suspeita')
elif positivas >= 3 and positivas <=4:
    print('Cúmplice')
elif positivas == 5:
    print('Assassino')
else:
    print('Inocente')