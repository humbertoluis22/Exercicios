notas = int(input('Informe a  quantidade de notas : '))
soma = 0 

for i in range(1,notas +1):
    nota = float(input(f'Informe a nota {i} : '))
    soma += nota

media = soma / notas
print(f'\nA media das notas é {media}\n')
