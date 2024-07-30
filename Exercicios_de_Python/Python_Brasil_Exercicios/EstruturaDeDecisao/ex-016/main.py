print('Equação de segundo grau \n')

a = int(input('informe o valor de A :'))
if a <= 0 :
    print('A Equação não é de segundo grau!')
else:
    b  = int(input('informe o valor de B: ')) 
    c = int(input('informe o valor de C : '))

    delta = b**2 - 4*a*c

    if delta < 0 :
        print('a equação não possui raizes reais')
    elif delta == 0 :
        print('equação possui apenas uma raiz real\n')
        raiz = -b / (2*a)
        print(f"o resultado é {raiz}")
    
    elif delta > 0 :
        x1 = (-b + (delta **2)) / (2*a)
        x2 = (-b - (delta ** 2)) / (2*a)

        print("a equação possui duas raiz reais\n")
        print(f'Primeira : {x1}')
        print(f'Segunda : {x2}')