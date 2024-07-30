numero_informado = int(input('Informe um numero entre 1 e 1000: '))

if numero_informado < 1 or numero_informado > 999:
    print('Numero invalido !!!!')
else: 

    centenas = numero_informado // 100
    dezenas = (numero_informado % 100 ) //10 
    unidades = (numero_informado % 10) // 1
    
    if centenas != 0  :
        print(f'{centenas} centenas e {dezenas} dezenas e {unidades} unidades')
    
    elif dezenas !=0 and centenas == 0 : 
        print(f'{dezenas} dezenas e {unidades} unidades')
    
    else:
        print(f'{unidades} unidades')