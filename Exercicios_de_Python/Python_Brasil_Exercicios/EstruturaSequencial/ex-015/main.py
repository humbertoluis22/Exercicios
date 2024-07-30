salario_hora = float(input('Informe o valor da sua trabalhada : '))
horas_mensal = float(input('Informe a sua carga horaria mensal : '))

salario_bruto = salario_hora * horas_mensal
imposto_renda = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
descontos =  imposto_renda + inss + sindicato
salario_liquido = salario_bruto - descontos

print(f"""
+ Salário Bruto : R$:{salario_bruto:.2f}
- IR (11%) : R$:{imposto_renda:.2f}
- INSS (8%) : R$:{inss:.2f}
- Sindicato ( 5%) : R$:{sindicato:.2f}
= Salário Liquido : R$:{salario_liquido:.2f}
""")