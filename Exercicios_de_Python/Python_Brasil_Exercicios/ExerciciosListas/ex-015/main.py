notas = []
notas_7 =  []

while True:
    nota = float(input('Insira uma nota : '))
    notas.append(nota)
    if nota < 7 :
        notas_7.append(nota)

    print('Deseja incluir uma nova nota? ')
    opcao = input('1- sim | 2 - não : ')
    if opcao == '2':
        print('TCHAU TCHAU :D\n')
        break

print(f'Quantidade de valores que foram lidos: {len(notas)}')
print(f'Valores na ordem em que foram informados :  {notas}')
print(f'valores na ordem inversa : ')
for i in range(0,len(notas)):
    print(notas[-i])
print(f'soma dos valores: {sum(notas)}')
print(f'média dos valores: {(sum(notas)/len(notas)):.2f}')
print(f'quantidade de valores acima da média calculada : {len([nota for nota in notas if nota > sum(notas)/len(notas) ])}')
print(f'quantidade de valores abaixo de sete : {len(notas_7)}')
print('ATÉ a proxima')