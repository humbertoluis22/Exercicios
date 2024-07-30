divida = float(input("Informe o valor da divida : "))
porcento = 0.05
qtd_parcelas = 0

print("Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela")
for i in range(1, 5 + 1):
    if i == 1:
        print(f"R$ {divida}             0               1               R$ {divida}")
    else:
        porcento += 0.05
        qtd_parcelas += 3
        print(
            f"R$ : {divida + (divida * porcento )}        {(divida * porcento):.2f}       {qtd_parcelas}           R$ {((divida + (divida * porcento ))/qtd_parcelas):.2f}"
        )
