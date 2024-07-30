nota1= float(input('Digite a primeira nota: '))
nota2= float(input('Digite a segunda nota: '))
media = (nota1 + nota2) /2

atribuicao = ''

if media >= 9 and media <=10:
    atribuicao = 'A'
elif media >= 7.5 and media <= 9.0:
    atribuicao = 'B'
elif media >= 6 and media <= 7.5:
    atribuicao = 'C'
elif media > 4 and media <= 6:
    atribuicao = 'D'
elif media <= 4 and media >= 0:
    atribuicao = 'E'

print(f'{'APROVADO' if atribuicao  in 'ABC' else 'REPROVADO'}')