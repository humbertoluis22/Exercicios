intervalos_valores = [
    ["200 - 299", []],
    ["300 - 399", []],
    ["400 - 499", []],
    ["500 - 599", []],
    ["600 - 699", []],
    ["700 - 799", []],
    ["800 - 899", []],
    ["900 - 999", []],
    ["1000", []],
]


while True:
    salario_semana = 200
    vedas_semana = float(input("Informe o valor da sua venda dessa semana : "))
    acrescimo_salario = vedas_semana * 0.09
    salario_receber = salario_semana + acrescimo_salario
    print(f"salario a receber: {salario_receber}")

    comparativo = int(str(salario_receber)[0]) - 2
    intervalos_valores[comparativo][1].append(1)

    print("Mais algum vendedor ira utilizar o sistema ? ")
    opcao = input("1 - sim | 2 - não : ")
    if opcao == "2":
        break

print("\nQuantidade de colaboradores que receberam entre os intervalos : ")
print(
    f"""
$200 - $299  :{sum(intervalos_valores[0][1])} 
$300 - $399  :{sum(intervalos_valores[1][1])} 
$400 - $499  :{sum(intervalos_valores[2][1])} 
$500 - $599  :{sum(intervalos_valores[3][1])}
$600 - $699  :{sum(intervalos_valores[4][1])}
$700 - $799  :{sum(intervalos_valores[5][1])}
$800 - $899  :{sum(intervalos_valores[6][1])}
$900 - $999  :{sum(intervalos_valores[7][1])}
$1000 em diante  : {sum(intervalos_valores[8][1])}
"""
)
