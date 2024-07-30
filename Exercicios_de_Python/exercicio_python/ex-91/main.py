def frequencia_palavra(frase: str) -> zip:
    """responsavel por verificar a frequencia com qual 
    cada palavra aparece dentro de um texto

    Parameters
    ----------
    frase : str
        frase a ser verificada

    Returns
    -------
    zip
        zip com as palavras e quantidade de frequencia
        palavra & frequencia
    """
    palavras = []
    quantidade = []
    frase_quebrada = frase.split()

    for palavra in frase_quebrada:
        if palavra not in palavras:
            palavras.append(palavra)
            quantidade.append(frase.count(palavra))
            continue

    palavra_quantidade = zip(palavras,quantidade)
    return palavra_quantidade


palavra_quantidade = frequencia_palavra('eu  eu amo eu amo chocolate')
for palavra,quantidade in palavra_quantidade:
    print(f'A palavra {palavra} apareceu {quantidade} vezes')