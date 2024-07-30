def altera_posicao(lista:list,posicao_base:int,posicao_troca:int)-> list:
    """altera  dois elementos de uma lista de posicao 

    Parameters
    ----------
    lista : list
        lista para fazer troca
    posicao_base : int
        primeira posição
    posicao_troca : int
        posicao de troca

    Returns
    -------
    list
        lista alterada
    """
    if len(lista) >=2 :
        try:
            lista2 = lista.copy()
            lista2[posicao_base] = lista[posicao_troca] 
            lista2[posicao_troca]  = lista[posicao_base]
            return lista2
        except Exception:
            print('Houve um erro na hora da troca, favor verificar posição escolhida...')
    
lista =  [11, 22, 33, 44, 55, 66, 77, 88, 99, 'X']

resultado = altera_posicao(lista,0,-1)
print(resultado)
