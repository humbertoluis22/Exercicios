contador = 0
maior = menor  = 0 
soma_notas = 0 

# respostas  = { 
# '1' : 'A',
# '2' : 'B',
# '3' : 'C',
# '4' : 'D',
# '5' : 'E',
# '6' : 'E',
# '7' : 'D',
# '8' : 'C',
# '9' : 'B',
# '10' : 'A'
# }

respostas = {}

for i in range(1,10+ 1):
    resposta_  = input(f'Informe a resposta da questao {i} : ').upper().strip()
    gabarito = { i : resposta_} 
    respostas.update(gabarito)

print()

while True:
    contador += 1
    acertos = 0 

    for i in range(1,11):
        resposta = input(f'Digite a resposta da questao {i} [A | B | C | D | E] : ').upper().strip()
        if resposta == respostas[str(i)]:
            acertos += 1

    soma_notas += acertos
    
    if contador == 1:
        maior = menor = acertos
    else:
        if acertos > maior:
            maior = acertos
        elif acertos < menor:
            menor = acertos

    print('Deseja utilizar novamente o sistema de notas ? ')
    opcao = int(input('[1-sim | 2- Não ]: '))
    if opcao == 2:
        break

print(f'***********************************************************************')
print(f'Total de alunos que utilizaram o sistema : {contador}')
print(f'Maior acerto : {maior}')
print(f'Menor acerto : {menor}')
print(f'Media de notas : {(soma_notas / contador):.2f}')
print('***********************************************************************')