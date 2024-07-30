def maior_valor(valor1:int,valor2:int,valor3:int)->int:
    """Retorna o maior valor entre tres valores
    
    Parameters
    ----------
    valor1 : int
        numero para comparação
    valor2 : int
        numero para comparação
    valor3 : int
        numero para comparação

    Returns
    -------
    int
        maior valor
    """
    lista = [valor1,valor2,valor3]
    return max(lista)



valores = maior_valor(2,5,3)
print(valores)