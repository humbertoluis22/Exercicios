import random

palavras = [
    "Maçã",
    "Banana",
    "Laranja",
    "Uva",
    "Manga",
    "Morango",
    "Abacaxi",
    "Melancia",
    "Pera",
    "Kiwi",
]
palavra_aleatoria = palavras[random.randint(0, 9)].lower().strip()
indice_letra = []
palavra_embaralhada = ""
cont = 1

while len(indice_letra) != len(palavra_aleatoria):
    indice = random.randint(0, len(palavra_aleatoria) - 1)
    if indice in indice_letra:
        continue
    indice_letra.append(indice)
    palavra_embaralhada += palavra_aleatoria[indice]

print(f"A palavra embaralhada é {palavra_embaralhada}")

while cont < 7:
    chute = input(f"Informe qual seu chute {cont} :").lower().strip()
    if chute == palavra_aleatoria:
        print("\nParabens vc acertou a palavra\n")
        print(f"A palavra era {palavra_aleatoria} !!!")
        break
    print("Não é essa a palavra ")
    cont += 1

if cont == 7:
    print("\nVoce perdeu !!!")
    print(f"A palavra era {palavra_aleatoria}\n")
