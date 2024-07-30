numeros = []
mult = 1 

for i in range(1, 6):
    numero = int(input(f"Digite o numero {i} : "))
    numeros.append(numero)
    mult *= numero

print(f'\nNUMEROS INFORMADOS : {" , ".join([str(numero) for numero in numeros])}')
print(f'SOMA DOS NUMEROS : {sum(numeros)}')
print(f'MULTIPLICAÇÃO DOS NUMEROS : {(mult)}')