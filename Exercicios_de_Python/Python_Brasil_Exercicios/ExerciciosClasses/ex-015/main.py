from tamagushi import Tamagushi

bicinho_virtual = Tamagushi('Rael',60,80,20,50)
bicinho_virtual.alterar_fome(90)
bicinho_virtual.alterar_nome('Gael')
bicinho_virtual.alterar_idade(10)
bicinho_virtual.alterar_saude(70)
bicinho_virtual.brincar(90)

nome = bicinho_virtual.retorna_nome()
fome = bicinho_virtual.retorna_fome()
idade = bicinho_virtual.retorna_idade()
saude = bicinho_virtual.retorna_saude()
tedio = bicinho_virtual.retorna_tedio()

print(f'nome : {nome}')
print(f'fome : {fome}')
print(f'idade : {idade}')
print(f'saude : {saude}')
print(f'tedio : {tedio}')
print(bicinho_virtual)