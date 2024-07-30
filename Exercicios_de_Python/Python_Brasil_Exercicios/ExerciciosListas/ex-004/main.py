letras = []
palavra = 'Apenas um teste'
valida_letra = []

for letra in palavra.replace(' ',''):
    letra = letra.upper()
    letras.append(letra)

for letra in letras:
    if letra not in 'AEIOU':
        valida_letra.append(letra)

print(f'Existem {len(valida_letra)} consoantes')