base = int(input('informe o valor da base : '))
expoente = int(input('informe o valor do expoente: '))

contador = 1

for i in range(0,expoente):
    contador *= base

print(f'resultado da potencia : {contador}')
