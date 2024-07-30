from texto import *

def contador_de_letras(texto:str) -> list:
    """conta qutas letras maisculas e minusculas
    uma palavra possui

    Parameters
    ----------
    texto : str
        texto ou palavra para calculo

    Returns
    -------
    list
        retonar uma lista de numeros,
        o primeiro elementos da lista sao as letras maisculas 
        e o segundo elemento da lista sao as minusculas
    """
    letras_maisculas = []
    letras_minusculas = []
    for  letra in texto:
        if letra.isalpha():
            if letra  == letra.upper():
                letras_maisculas.append(letra)
            if letra == letra.lower():
                letras_minusculas.append(letra)
    
    quantidades = [len(letras_maisculas),len(letras_minusculas)]
    return quantidades


texto = texto_exemplo
resultado = contador_de_letras(texto)
print(resultado)
print(f'a palavra ou texto tem {resultado[0]} letras maisculas')
print(f'a palavra ou texto tem {resultado[1]} letras minusculas')