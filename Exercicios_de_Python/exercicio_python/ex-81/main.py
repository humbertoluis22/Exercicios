from numeros_extensos import * 

numero = input('digite um numero  : ')


if int(numero) < 20 :
    print(numeros_ate_19[numero])

elif int(numero) >= 20 and int(numero) < 100:
    if numero[1] == '0':
        print(numeros_dezenas_zero[numero])
    else:    
        print(
            f'{numeros_dezenas[numero[0]]}'
            + f' {numeros_ate_19[numero[1]]}'
            )
    
elif int(numero) >= 100:
    if numero[1] and numero[2] == '0':
        print(f'{numeros_centenas_zero[numero]}')
    elif numero[1] == '0':
        print(f'{numeros_centenas[numero[0]]} e {numeros_ate_19[numero[2]]}')
    else:    
        print(
            f'{numeros_centenas[numero[0]]} e '+
            f' {numeros_dezenas[numero[1]]}'+
            f' {numeros_ate_19[numero[2]]}'
            ) 