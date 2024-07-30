numero_dia = int(input('digite um numero entre 1 e 7 : '))

if numero_dia < 1  or numero_dia > 7:
    print('Numero inválido')
elif numero_dia == 1: 
    print('domingo')
elif numero_dia == 2:
    print('segunda')
elif numero_dia == 3:
    print('terça')
elif numero_dia == 4:
    print('quarta')
elif numero_dia == 5:
    print('quinta')
elif numero_dia == 6:
    print('sexta')
elif numero_dia == 7:
    print('sabado')