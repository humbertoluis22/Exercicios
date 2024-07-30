numero = int(input('digite um numero : '))
dicionario = {}

for i in range(1,numero+1):
    dicionario_apoio = {i : i * i}
    dicionario.update(dicionario_apoio)

print(dicionario)