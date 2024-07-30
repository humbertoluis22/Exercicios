unidades = ["", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove"]
especiais = ["dez", "onze", "doze", "treze", "catorze", "quinze", "dezesseis", "dezessete", "dezoito", "dezenove"]
dezenas = ["", "", "vinte", "trinta", "quarenta", "cinquenta", "sessenta", "setenta", "oitenta", "noventa"]

numero  = int(input('Digite um numero entre  1-99 : '))

if numero >= 1 and numero <=9:
    print(f'\n{unidades[numero]}\n') 
     
elif numero >= 10 and numero <= 19:  
    indice = numero % 10
    print(f'\n{especiais[indice]}\n')

elif numero >=20 and numero <= 99:
    indice_unidade = numero % 10
    indice_decimal = numero // 10
    print(
        f'\n{dezenas[indice_decimal]} ' +
        f'{f"e {unidades[indice_unidade]}" if indice_unidade > 0 and indice_decimal > 2 else unidades[indice_unidade]}\n'
        )  
else:
    print('Numero inválido')