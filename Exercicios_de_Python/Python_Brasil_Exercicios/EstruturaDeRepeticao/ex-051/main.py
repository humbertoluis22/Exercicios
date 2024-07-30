s = '1/1'
soma_1  = 0 
soma_2  = 0 
 
for i in range(1,11):
    if i == 1:
        s = s.split('/')
        numero_1 = int(s[0])
        numero_2 = int(s[1])
    soma_1 += numero_1
    soma_2 += numero_2
    print(f'{numero_1}/{numero_2}',end=' + ')
    numero_1 += 1
    numero_2 += 2
    if i == 10:
        print('... + n/m')

print('\nA soma dos numeros : ')
print(f'=> {soma_1}/{soma_2}')