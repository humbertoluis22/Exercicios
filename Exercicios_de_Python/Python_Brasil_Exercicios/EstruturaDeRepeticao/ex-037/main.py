soma_altura =soma_peso = 0

contador = 0 

maior = menor = 0
codigo_maior = codigo_menor = 0 

gordo = magro  = 0 
codigo_gordo = codigo_magro = 0 

while True:
    codigo = int(input('Informe seu codigo : '))
    altura = float(input('Informe sua altura: '))
    peso = float(input('informe seu peso : '))
    
    soma_altura += altura
    soma_peso += peso
    contador += 1

    if contador == 1:
        maior = menor = altura
        gordo = magro = peso
        codigo_maior = codigo_menor = codigo
        codigo_gordo = codigo_magro = codigo

    if altura > maior:
        maior = altura
        codigo_maior = codigo
    elif altura < menor :
        menor = altura
        codigo_menor = codigo
    
    if peso > gordo: 
        gordo = peso
        codigo_gordo = codigo
    elif peso < magro:
        magro = peso
        codigo_magro = codigo

    print('Tem outro alunos ?')
    opcao = int(input('[0 - Não | 1 - sim ] : '))
    if opcao == 0:
        print('TCHAU TCHAU :D!!!')
        break

media_peso = soma_peso / contador
media_altura = soma_altura / contador

print(f'\nO peso medio dos alunos é {media_peso:.2f}')
print(f'A altura media dos alunos é {media_altura:.2f}')
print(f'O aluno mais alto é {codigo_maior} que tem {maior:.2f} de altura')
print(f'O aluno mais baixo é {codigo_menor} que tem {menor:.2f} de altura')
print(f'O aluno mais gordo é {codigo_gordo} quem pesa {gordo} KG')
print(f'O aluno mais magro é {codigo_magro} quem pesa {magro} KG\n')