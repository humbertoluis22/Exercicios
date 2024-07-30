def  metade_numero (numero):
    return[numero //2, numero -numero//2]

numero = int(input('digite um numero : '))
metade = metade_numero(numero)
print(metade)