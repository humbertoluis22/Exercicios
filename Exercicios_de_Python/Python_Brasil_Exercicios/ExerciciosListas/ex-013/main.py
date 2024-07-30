from meses import * 


soma_temperatura = 0 
temperatura_mes = []

for i in range(0,12):
    temperatura = int(input(f'informe a temperatura de {meses[i]} : '))
    temp_mes = [temperatura,meses[i]]
    temperatura_mes.append(temp_mes)
    soma_temperatura += temperatura

print()
media_temperatura = soma_temperatura/ 12

print(f'Meses em que a temperatura foi a cima da media de {(media_temperatura):.1f} !')
print(f'Meses : ')
for temperatura,mes in temperatura_mes:
    if temperatura > media_temperatura:
        print(mes)


