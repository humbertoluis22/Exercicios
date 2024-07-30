n1 = int(input('Digite o valor do primeiro lado  : '))
n2 = int(input('Digite o valor do segundo lado  : '))
n3 = int(input('Digite o valor do terceiro lado  : '))

if (any([n1 + n2 > n3 , n2 + n3 > n1, n1 + n3 > n2])
     and  
    any([n1 == n2,n2 == n3,n3== n1])
    ):
    print('Forma um triangulo Isósceles ')

elif (
    any([n1 + n2 > n3 , n2 + n3 > n1, n1 + n3 > n2]) and
    n1 == n2 == n3
      ):
    print('Forma um triangulo Equilátero ')

elif (
    any([n1 + n2 > n3 , n2 + n3 > n1, n1 + n3 > n2]) and
    n1 != n2 != n3
    ):
    print('Forma um triangulo Escaleno ')
else:
    print('Não forma um triangulo!! ')