import random

frutas = [
    "banana",
    "abacaxi",
    "mamao",
    "uva",
    "morango",
    "manga",
    "laranja",
    "pera",
    "melancia",
    "abacate",
]
palavra_secreta = []

nome_fruta = []
cont = 0
acerto = 0

indice_aleatorio = random.randint(0, 9)
palavra_secreta = frutas[indice_aleatorio]

for letra in palavra_secreta:
    nome_fruta.append(" _ ")

v_letra = []

while cont < 6:
    print(f"{" ".join(nome_fruta)}")
    print()
    chute = input("Digite uma letra : ").lower()

    if chute in v_letra:
        print("Essa letra ja foi informada !!!")
        continue
    elif chute in palavra_secreta:
        for indice, letra in enumerate(palavra_secreta):
            if letra == chute:
                v_letra.append(letra)
                nome_fruta[indice] = chute
                acerto += 1
        if acerto == len(nome_fruta):
            print("Parabens voce ganhou !!!")
            print(f"A palavra era : {palavra_secreta}\n")
            break

        continue

    cont += 1
    pass

if cont == 6:
    print("Você Perdeu !!!")
