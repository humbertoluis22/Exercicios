import random

def embaralha_palavra(palavra:str)-> str:
    """Embaralha a palavra informada p
 
    Args:
        palavra (str): somente uma palavra 
        pode ser informada 
        ex: python 
    
    Returns:
        str: palavra embaralhada
    """
    valida_letra = []
    palavra_embaralhada =''
    while True:
        posicao = random.randint(0,len(palavra)-1)
        if palavra[posicao] in valida_letra:
            continue
        valida_letra.append(palavra[posicao])
        palavra_embaralhada += palavra[posicao]

        if len(palavra) == len(palavra_embaralhada):
            break
        
    return palavra_embaralhada

palavra_embaralhada = embaralha_palavra('humberto')
print(f'Palavra embaralhada : {palavra_embaralhada}')