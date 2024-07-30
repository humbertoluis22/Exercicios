import random

numeros = []
numeros_verificacao = []
numero_quantidade = []

for i in range(0,100):
    numero = random.randint(1,6)
    numeros.append(numero)

for numero in numeros:
    if numero in numeros_verificacao:
        continue
    numeros_verificacao.append(numero)
    qtd_num = numeros.count(numero)
    numero_quantidade.append([numero,qtd_num])


for num,qtd in numero_quantidade:
    print(f'Numero: {num} - Quantidade {qtd }')