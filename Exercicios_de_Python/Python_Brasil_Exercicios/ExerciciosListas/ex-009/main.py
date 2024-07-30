a = []
b = []
for i in range(0,10):
    numero = int(input('Informe um numero  :'))
    a.append(numero)
    b.append(numero ** 2)

print('\n*******************************')
print(f'numeros inseridos = {' , '.join([str(numero) for numero in a])}')
print(f'numeros elevado ao quadrado = {' , '.join([str(n) for n in b])}')
print(f'Soma dos quadrados  = {sum(b)}')
print('*******************************\n')