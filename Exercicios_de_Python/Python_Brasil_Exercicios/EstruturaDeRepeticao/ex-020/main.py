while True:
    numero = -1
    while numero < 0 or numero > 1000:
        numero = int(input('informe o numero para fatorial [1 - 16]: '))
    
    contador = 0 
    
    for i in range(1,numero -1 ):
        if i == 1:
            contador = numero * (numero - i)
        else:
            contador *= numero - i 
    
    print(f'\nO fatorial do numero {numero} é {contador}\n')
    
    opcao = int(input('deseja efetuar uma nova operação [1-SIM | 2 - NÃO] :'))
    if opcao == 2:
        print('TCHAU TCHAU :D')
        break