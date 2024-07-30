salario = float(input('Informe o seu salario : '))
ano_contratado = 1995
ano_atual = 2024
taxa_aumento = 0
salario_atual = 0

for i in range(ano_contratado + 1,ano_atual + 1):
    if i == 1996 :
        taxa_aumento = 0.015
        salario_atual = (taxa_aumento * salario) + salario
        print(salario_atual)
    else:
        taxa_aumento *= 2 
        salario_atual = (taxa_aumento * salario_atual) + salario_atual 
        print(f'Salario atual : {salario_atual:.2f}')
        62,727