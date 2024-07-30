from tamagushi import Tamagushi

bicinho_virtual = Tamagushi('Rael',60,80,20)
bicinho_virtual.alterar_fome(90)
bicinho_virtual.alterar_nome('Gael')
bicinho_virtual.alterar_idade(10)
bicinho_virtual.alterar_saude(70)

nome = bicinho_virtual.retorna_nome()
fome = bicinho_virtual.retorna_fome()
idade = bicinho_virtual.retorna_idade()
saude = bicinho_virtual.retorna_saude()

print(nome)
print(fome)
print(idade)
print(saude)