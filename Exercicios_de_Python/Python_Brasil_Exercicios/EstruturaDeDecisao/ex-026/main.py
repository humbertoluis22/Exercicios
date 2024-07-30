print('Posto de Gasolina')

print('Escolha o combustivel')

tipo_combustivel  = input('A-álcool, G-gasolina : ').upper().strip()
if tipo_combustivel not in 'AG':
    print('Opção de combustivel invalida')
    exit()
try:
    quantidade_litros = int(input('Informe a quantidade de litros : '))
except:
    print('Valor ou Opcao invalido!!')


if tipo_combustivel == 'A' and quantidade_litros <= 20 :
    porcentagem_desconto = 0.03 
elif tipo_combustivel == 'A' and quantidade_litros > 20 :
    porcentagem_desconto =  0.05
elif  tipo_combustivel == 'G' and quantidade_litros  <= 20:
    porcentagem_desconto = 0.04
elif tipo_combustivel =='G' and quantidade_litros > 20 :
    porcentagem_desconto = 0.06

if tipo_combustivel == 'A':
    valor_litro = 1.90
elif tipo_combustivel =='G':
    valor_litro = 2.50

desconto_litro = valor_litro * porcentagem_desconto 
valor_desconto  = desconto_litro * quantidade_litros

print(f'Você recebeu R$:{valor_desconto:.2f} de desconto ')
print(f'Valor sem desconto : R$:{(valor_litro * quantidade_litros):.2f}')
print(f'Valor com desconto: R$:{((valor_litro * quantidade_litros) - valor_desconto):.2f}')




