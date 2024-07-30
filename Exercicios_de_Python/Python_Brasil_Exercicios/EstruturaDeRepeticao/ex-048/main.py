numero =  input('Informe um numero inteiro : ')
numero_contrario = ''

if not  numero.isnumeric():
    print('Numero invalido')
for i in range(1,len(numero) + 1):
    numero_contrario += numero[-i]

print('Numero ao contrario:')
print(f'=> {numero_contrario}')