def verifica_palavra(palavra_varificacao:str,texto:str)->bool:
    """verifica se uma palavra existe ou não dentro de um texto,
    desconsiderando qualquer caracter que nao seja uma string de A-Z

    Parameters
    ----------
    palavra : str
        palavra a ser verificada dentro de um texto
    texto : str
        texto para fazer a verificação

    Returns
    -------
    bool
        Verdadeiro caso encontre a palavra 
        falso se nao encontrar
    """
    for palavra in texto.split():
        if palavra.isalpha():
            if palavra.upper() == palavra_varificacao.upper():
                return True
    return False
            

texto = 'Função simples mas talvez seja útil'
resultado = verifica_palavra('talvez',texto)
if resultado:
    print('palavra encontrada')
else:
    print('OPS.. não foi encontrado')