print('\nFatorial')

numero = int(input('informe um numero  : '))
cont = 1 

for i in range(1, numero - 1):
    if i == 1 :
        numero_esperado = numero *( numero - i )
    else:
        numero_esperado *= (numero -i)
    
print(f'Resultado : {numero_esperado}')