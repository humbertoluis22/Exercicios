from funcionario import Funcionario

f1= Funcionario('Humberto',3500.00)
salario = f1.retorna_salario()
nome = f1.retorna_nome()
print(salario)
print(nome)
f1.aumentar_salario(15)
novo_salario = f1.retorna_salario()
print(novo_salario)