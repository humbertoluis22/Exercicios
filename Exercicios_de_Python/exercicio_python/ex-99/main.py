try:
    horas_trabalhadas  = int(input('Informe a quantidade de horas trabalhadas : '))
    salario = 0 
    if horas_trabalhadas > 40: 
        horas_extras = horas_trabalhadas - 40 
        salario = (horas_trabalhadas * 29.11) + ( horas_extras * 5)
    else:
        salario = horas_trabalhadas * 29.11
except:
    print('digite apenas valores numericos!!')
    exit() # encerra um programa ao ser executada | usar apenas para testes

print(f'valor por hora trabalhada: {horas_trabalhadas * 29.11:.2f}')
print(f'valor hora extra = R$: {horas_extras*5:.2f}')
print(f'Salario a receber  =   R$: {salario:.2f}')
