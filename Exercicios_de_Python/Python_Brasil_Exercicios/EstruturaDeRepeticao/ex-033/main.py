temperaturas = input('Informe a quantidade de temperaturas : ')
maior = 0
menor = 0 
soma = 0 

if not temperaturas.isnumeric():
    print('Valor invalido')
else:
    temperaturas = int(temperaturas)
    for i in range(1,temperaturas+1):
        temperatura = int(input(f'Informe a temperatura {i} : '))
        soma += temperatura
        if i ==1 :
            maior = menor = temperatura
        else:
            if temperatura > maior :
                maior = temperatura
            elif temperatura < menor :
                menor = temperatura
        
media_temperatura = soma / temperaturas

print(f'\nA maior temperatura informada foi {round(maior)}ºC')
print(f'A menor temperatura informada foi {round(menor)}ºC')
print(f'A media de temperaturas é {round(media_temperatura)}ºC\n')