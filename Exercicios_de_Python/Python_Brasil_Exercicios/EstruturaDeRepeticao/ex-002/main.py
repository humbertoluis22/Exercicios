while True:
    print('informe seu nome !')
    nome= input('nome : ').strip().lower()
    print('\ninforme sua senha !')
    senha = input('senha : ').strip().lower()
    
    if senha == nome:
        print('***************************************')
        print('\nA sua senha não pode ser seu nome !\n')
        print('***************************************')
    else:
        break