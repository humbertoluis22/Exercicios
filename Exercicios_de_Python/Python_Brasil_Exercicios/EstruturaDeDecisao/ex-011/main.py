salario = float(input('Informe o seu salário: '))
percentual  = ''
novo_salario = 0
valor_aumentado = 0 

if salario <= 280:
    percentual = '20%'
    valor_aumentado = salario * 0.2
    novo_salario = salario + valor_aumentado
   
elif salario > 280 and salario <= 700:
    percentual = '15%'
    valor_aumentado = salario * 0.15
    novo_salario = salario + valor_aumentado
    #15
elif salario > 700 and salario <= 1500:
    percentual = '10%'
    valor_aumentado = salario * 0.1
    novo_salario = salario + valor_aumentado
    #10
elif salario >  1500:
    percentual = '5%'
    valor_aumentado = salario * 0.05
    novo_salario = salario + valor_aumentado
    #5

print(f'salário antes do reajuste : {salario}')
print(f'percentual de aumento aplicado: {percentual}')
print(f'valor do aumento: {valor_aumentado}')
print(f'novo salário: {novo_salario}')