idades = []
alturas = []

for i in range(1,5+1):
    idade = int(input('Informe a sua idade : '))
    altura = float(input('Informe a sua altura : '))
    idades.append(idade)
    alturas.append(altura)

print('\n***********************************************')
print('ORDEM DE INSERÇÃO : ')
print(f'Idades : {idades}')
print(f'Alturas : {alturas}')
print()
print('ORDEM INVERSA : ')
print(f'idades : {sorted(idades,reverse=True)}')
print(f'alturas : {sorted(alturas,reverse=True)}')
print('***********************************************')