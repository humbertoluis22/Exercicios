situacao = [
    "",
    "necessita da esfera                 ",
    "necessita de limpeza                ",
    "necessita troca do cabo ou conector ",
    "quebrado ou inutilizado  ",
]

necessidades = []
valida_necessidades = []
situacao_necessidade = []
cont = 0 

print(
    """
1- necessita da esfera                 
2- necessita de limpeza                
3- necessita troca do cabo ou conector 
4- quebrado ou inutilizado 
"""
)

while True:
    necessidade = input("qual a necessidade do mouse [ex : 1] [0-encerrar]: ")
    if necessidade == "0":
        print("TCHAU TCHAU :p")
        break
    elif not necessidade.isnumeric() or int(necessidade) < 1 or int(necessidade) > 4:
        print('Necessidade inváldia!!')
        continue
   
    necessidades.append(int(necessidade))

total_mouse = len(necessidades)

for necessidade in necessidades:
    if necessidade in valida_necessidades:
        continue
    valida_necessidades.append(necessidade)
    situacao_necessidade.append(
        [situacao[necessidade], necessidades.count(necessidade)]
    )

print(f"\nQuantidade de mouses: {total_mouse}\n")
print("Situação                        Quantidade              Percentual")

for situacao, qtd_necessidade in situacao_necessidade:
    cont += 1
    print(f'{cont} - {situacao:<15} {qtd_necessidade:<15}  {((qtd_necessidade/len(necessidades))*100):.1f}%')