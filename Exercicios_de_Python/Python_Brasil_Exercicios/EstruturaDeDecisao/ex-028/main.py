print('Mercado tabajara\n')

print('Me informe qual o tipo da carne !!')
opcao_carne = input('1-File Duplo | 2-Alcatra | 3-Picanha: ').strip()

if (not opcao_carne.isnumeric 
            or opcao_carne not in '123'):
    print('Opção de carne invalida !!')

kg_carne = float(input('Digite a quantidade de kg : '))
cartao = input('possuir cartao tabajara? [1-sim|2-não] : ')

if (not cartao.isalnum() or
    cartao not in '12'):
    print('Opção de cartãop inválida!')

if (opcao_carne == '1'  and kg_carne <=5 ):
    valor_kg = 4.9
elif (opcao_carne =='1' and kg_carne > 5):
    valor_kg = 5.80
elif (opcao_carne =='2' and kg_carne <= 5):
    valor_kg = 5.90
elif (opcao_carne =='2' and kg_carne > 5):
    valor_kg = 6.80
elif(opcao_carne == '3' and kg_carne <=5):
    valor_kg = 6.9
elif(opcao_carne == '3' and kg_carne > 5):
    valor_kg = 7.80

valor_total  = kg_carne * valor_kg

print(f'\nO valor da compra foi de R$: {valor_total:.2f}')
if cartao == '1':
    desconto_cartao = valor_total * 0.05 
    print(f'valor de desconto R$:{desconto_cartao:.2f}')
    print(f'valor a pagar R$:{(valor_total - desconto_cartao):.2f}')
