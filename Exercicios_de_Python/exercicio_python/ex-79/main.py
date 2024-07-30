def maior_string(primeira_p:str, segunda_p:str)->str:
    """verifica maior string
    caso as strings tenham o mesmo tamanho 
    retorna as duas 

    Args:
        primeira_p (str): palavra aleatoria para comparalçao
        segunda_p (str): palavra aleatoria para comparalçao

    Returns:
        str: string de maior tamanho
    """

    if len(primeira_p) > len(segunda_p):
        return primeira_p
    elif len(primeira_p) < len(segunda_p):
        return segunda_p
    elif len(primeira_p) == len(segunda_p):
        return primeira_p,segunda_p
    

comparacao = maior_string('fazendo o primeiro  teste ','segundo teste')
print(comparacao)