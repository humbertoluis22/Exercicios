def americano_nome(nome:str,sobrenome:str) -> str:
    """Responsavel por inverte os nomes
    para deixar em padrao americado 

    Args:
        nome (str): primeiro nome do usuario
        sobrenome (str): sobre nome usuario

    Returns:
        str: retorna uma string com os nomes invertidos
    """
    return f'{sobrenome} {nome}'


nome = input('digite seu primeiro nome : ')
sobre_nome = input('digite seu sobrenome : ')

exibicao_america = americano_nome(nome,sobre_nome)
print(exibicao_america)
