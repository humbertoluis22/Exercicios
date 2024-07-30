numero = input('Informe um número para fatorial : ')
if not numero.isnumeric():
    print('Numero invalido')

cont = 0 
numero = int(numero)
print(f'{numero}! =',end= ' ')
for i in range(1,numero-1):
    if not i == 1 :
        cont *= (numero - i)
    else:
        cont = numero * (numero - i)
        print(f'{numero}',end= ' . ')
    print(f'{numero - i}',end= ' . ')
print(f'1 = {cont}')

