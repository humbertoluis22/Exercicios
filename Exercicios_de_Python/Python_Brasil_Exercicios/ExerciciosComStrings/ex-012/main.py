print('Valida e corrige número de telefone\n')
print('Digite seu numero de telefone no formato :')
numero_telefone = input('xxxx-xxxx :  ').strip().replace('-','')
n_inicial = '3'
    
if len(numero_telefone) > 8 :
    print('Numero invalido')
    exit()
elif len(numero_telefone) < 8:
    print(f'\nTelefone possui {len(numero_telefone)} dígitos.' +
          'Vou acrescentar o digito três na frente.\n')
    numero_telefone = numero_telefone.zfill(8)
    novo_telefone = n_inicial + numero_telefone[1:]
else:
    novo_telefone = numero_telefone
    
print(f'Telefone corrigido sem formatação: {novo_telefone[:4]}{novo_telefone[4:]}')
print(f'Telefone corrigido com formatação: {novo_telefone[:4]}-{novo_telefone[4:]}\n')

