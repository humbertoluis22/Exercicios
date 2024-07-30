numeros = []
par = []
impar = []

for i in range(1,20+1):
    numero = int(input('Digite um numero : '))
    numeros.append(numero)
    if numero % 2 == 0 :
        par.append(numero)
    else:
        impar.append(numero)

print(f'\nLISTA DE NUMEROS : {numeros}')
print(f'LISTA DE NUMEROS PARES : {par}')
print(f'LISTA DE NUMEROS IMPARES : {impar}\n')