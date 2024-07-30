
serie = '1 + 1'
for i in range(0,15):
    if i  == 0 :
        print(serie,end = ' / ')
        serie = serie.split('+')
        numero_1 = int(serie[0])
        numero_2 = int(serie[1])
        
    numero_1 += numero_2
    print(f'{numero_1} + {numero_2}',end= '/ ' )
    if i == 14:
        print(' ... + 1/N')