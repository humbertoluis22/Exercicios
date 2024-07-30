def  valor_ao_quadrado(numero)-> int:
    '''
    a entrada é um numero int e 
    saida int 
    função pra elevar o valor recebido ao quadrado
    '''
    return numero **2

numero = int(input('digite um valor : '))

valor = valor_ao_quadrado(numero)
print(valor)