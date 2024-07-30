def somaImposto(taxaImposto: float,custo:float) ->float:
    """Soma o valor do produto com a taxa de imposto 

    Args:
        taxaImposto (float): Quantia em porcentagem de imposto exemplo 17.5 
        custo (float): Valor do produto

    Returns:
        float: Valor do produto com as taxa de imposto calculadas
    """
    
    imposto = taxaImposto / 100
    novo_valor = (custo*imposto) + custo

    return novo_valor

valor_atualizado = somaImposto(17.5,100)
print(valor_atualizado)