nome = [input('digite um nome: ')]
notas = [int(nota) for  nota in  input('digite duas notas separadas por virgula : ').split(',')]
nome_nota = zip(nome,notas)
for nome,nota in nome_nota:
    print(f'{nome}: {notas}')