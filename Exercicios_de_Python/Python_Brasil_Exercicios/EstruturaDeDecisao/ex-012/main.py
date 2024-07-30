print('Folha de pagamento')

valor_hora = float(input('Digite o valor da sua hora : '))
horas_mes =  float(input('Digite sua carga horaria mensal : ')) 
ir = 0
salario_bruto  = valor_hora * horas_mes

if salario_bruto <= 900:
    ir = 0
elif salario_bruto <= 1500:
    ir = 0.05
elif salario_bruto <=2500:
    ir = 0.1
elif salario_bruto > 2500:
    ir = 0.2

valor_ir = salario_bruto * ir
inss = salario_bruto * 0.1
fgts = salario_bruto * 0.11
total_desconto = valor_ir + inss 

print(
    f"""
Sálario bruto: {salario_bruto}
(-) IR ({str(ir).split('.')[-1] if ir != 0 else ''}% )        : R$ {valor_ir:.2f}
(-) INSS (10%)                  : R$ {inss:.2f}
FGTS (11%)                      : R$ {fgts:.2f}
Total de descontos              : R$ {total_desconto:.2f}
Salário Liquido                 : R$ {salario_bruto - total_desconto:.2f}
    """

)