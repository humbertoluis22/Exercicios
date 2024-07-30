def numero_quadrado(numero:int)->int:
    """funçaõ para elevar um numero ao quadrado

    Parameters
    ----------
    numero : int
        numero que sera elevado 

    Returns
    -------
    int
        numero elevado ao quadrado 
    """
    return numero ** 2



numero = int(input('digite um numero :'))
num_quadrado = numero_quadrado(numero)
print(f'O numero {numero} elevado ao quadrado é {num_quadrado}')
