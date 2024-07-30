notas = []

for i in range(1,5):
    nota = float(input(f'Digite a nota {i} : '))
    notas.append(nota)

media = sum(notas)/len(notas)

print(f'\nNotas : {' , '.join([str(nota) for nota in notas])}')
print(f'Média : {media}')
