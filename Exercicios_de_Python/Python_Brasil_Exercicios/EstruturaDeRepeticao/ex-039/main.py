numero_alto = numero_baixo = 0
maior = menor = 0

for i in range(1, 10 + 1):
    numero = int(input("Informe o numero do aluno (numero inteiro) : "))
    altura = float(input("Informe a altura do aluno : "))
    if i == 1:
        maior = menor = altura
    if altura > maior:
        maior = altura
        numero_alto = numero
    elif altura < menor:
        menor = altura
        numero_baixo = numero

print(f"O aluno mais alto é {numero_alto} com a altura de {maior:.2f} de altura ")
print(f"O aluno mais baixo é {numero_baixo} com a altura de {menor:.2f} de altura ")
