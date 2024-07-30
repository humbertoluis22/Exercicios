numero = int(input('Informe um numero : '))
contador = 0 
conjunto_str = ''

for i in range(2,numero + 1):
    if numero % i == 0 :
        contador +=1
        if not i == numero:
            str_n = str(f'{i}')
            conjunto_str += str_n
        
if contador == 1:
    print(f'\nO numero {numero}  É PRIMO !!')
else: 
    print(f'\nO numero {numero} NÂO É PRIMO !!')
    n_divisiveis = ','.join(conjunto_str)
    print(f'É divisivel  por {n_divisiveis}\n')