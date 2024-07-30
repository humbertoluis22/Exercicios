import random

quantidade = int(input('escolha o tamanho da sua senha: '))
senha = []

for i in range(quantidade):
    senha.append(str(random.randint(1,10)))

senha = ''.join(senha)
print(senha)