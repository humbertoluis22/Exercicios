print('Verificando se o ano é  bissexto ')
ano_informado:str = input('Informe um ano aleatorio : ')

if (not ano_informado.isalnum or
    len(ano_informado) != 4
    ) : 
    print('Informe um ano valido !! ')
else: 
    verificar_digitos = int(ano_informado[2:])
    if verificar_digitos % 4 == 0 :
        print('Ano bissexto')
    else:
        print('Não é bissexto')
    
