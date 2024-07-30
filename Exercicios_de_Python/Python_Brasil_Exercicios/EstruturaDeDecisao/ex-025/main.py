print('Interrogatorio!! \n')

cont = 0 

print('"Telefonou para a vítima?"')
pergunta_1 = int(input('1-SIM | 2-NÃO : '))
if pergunta_1 == 1 : 
    cont += 1

print('Esteve no local do crime?')
pergunta_2 = int(input('1-SIM | 2-NÃO : '))
if pergunta_2 == 1:
    cont += 1

print('Mora perto da vítima?')
pergunta_3 = int(input('1-SIM | 2-NÃO : '))
if pergunta_3 == 1:
    cont +=1 

print('Devia para a vítima?')
pergunta_4 = int(input('1-SIM | 2-NÃO : '))
if pergunta_4 == 1: 
    cont +=1 

print('Já trabalhou com a vítima?')
pergunta_5 = int(input('1-SIM | 2-NÃO : '))
if pergunta_5 == 1: 
    cont += 1

if cont  == 2 : 
    print('\nSuspeita\n')
elif cont >= 3 and cont <= 4: 
    print('\nCúmplice\n') 
elif cont == 5:
    print('\nAssassino\n')
else:
    print('\nInocente\n')