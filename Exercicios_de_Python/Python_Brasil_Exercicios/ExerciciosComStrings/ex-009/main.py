import re

print('Digite o CPF no formato xxx.xxx.xxx-xx !!')
cpf = input('cpf : ')

cpf_verificado = re.findall(r'\d{3}.\d{3}.\d{3}-\d{2}',cpf)

if len(cpf_verificado) != 0:
    print('Cpf valido !!')
else:
    print('Cpf Invalida!!')
