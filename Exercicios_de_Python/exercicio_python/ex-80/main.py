from morse import *

palavra = input('digite a palavra para converte em codigo morse : ').upper()
palavra_codificada = ''

for letra in palavra:
    palavra_codificada += codigo_morse[letra]

print()
print(f'Palavra digitada : {palavra} ')
print("*********************************************************")
print(f'palavra codificada: {palavra_codificada}')