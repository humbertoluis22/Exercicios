from datetime import datetime

def tempo_execucao(funcao):
    def wrapper(*args,**kwargs):
        data_inicial = datetime.now().strftime("%H%M%S%f")
        data_inicial = datetime.strptime(data_inicial,"%H%M%S%f")
        resultado = funcao(*args,**kwargs)
        data_fim = datetime.now().strftime("%H%M%S%f")
        data_fim = datetime.strptime(data_fim,"%H%M%S%f")
        print(f'tempo de execução {data_fim - data_inicial} !!!')
        return resultado
    return wrapper


@tempo_execucao
def pesquisa_binaria(lista : list,item:int) -> int:
    """
    ira realizar a busca da posicao de um item 
    em uma lista ordenado
    caso encontre retorna a posição do item
    caso contrario retorna None
    """
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = round((baixo + alto) / 2)
        chute = lista[meio]
        if chute == item:
            return meio

        if chute > item:
            alto = meio - 1 
        else:
            baixo = meio + 1
    return None


@tempo_execucao
def pesquisa(lista: list,item:int) -> int:
    """
    ira percorrer a lista a procura do indice do item
    caso encontro retorna a posicao do item
    caso contrario retorna None
    """
    for i in range(len(lista)):
        if lista[i] == item:
            return i
    return None


lista = [1,3,5,7,9]
lista2 =[i for i in range(100000000)] 

local = pesquisa(lista2,99000000)
print(local)

local_binario = pesquisa_binaria(lista2,99000000)
print(local_binario)