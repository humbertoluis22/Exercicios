numero = int(input("Informe um numero inteiro : "))
numeros_primos = ""

for i in range(2, numero + 1):
    cont = 0
    for y in range(2, i+1):
        if i % y == 0:
            cont += 1
    n = str(i)
    if cont == 1:
        numeros_primos += n
    
print(f'\nNo intervalo de 1 a {numero}')
print(f'Os numeros primos são : {numeros_primos}\n')