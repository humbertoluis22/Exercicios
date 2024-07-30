numero = int(input('Informe um numero: '))
numeros_primos  = ''
numeros_divisiveis = ''

for i in range(2,numero+1):
    contador = 0 
    for y in range(2,i+1):
        if i % y == 0:
            contador +=1 
    n = str(i)
    if contador == 1:
        numeros_primos += n
    else:
        numeros_divisiveis += n

print(f'numeros primos : {numeros_primos}')
print(f'numeros divisiveis : {numeros_divisiveis}')