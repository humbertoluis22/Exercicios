def ordena_lista(numeros:list) -> list:
    """função para ordenar uma lista de numeros
    aleatorios  de forma crescente 

    Parameters
    ----------
    numeros : list
        lista de numeros aleatorios

    Returns
    -------
    list
        lista ordenada de forma crescente
    """

    lista_ordenada = sorted(numeros)
    return lista_ordenada

numeros = [1,4,5,3,6,56,3,73,45,8,9]
numeros_ordenados = ordena_lista(numeros)
print(numeros_ordenados)