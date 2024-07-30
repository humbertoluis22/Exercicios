def positivo_negativo(numero : float) -> str:
    """Verifica se o numero é positivo ou negativo

    Args:
        numero (float): numero para verificação

    Returns:
        str: P -> positivo N -> negativo
    """

    if numero <= 0 :
        return 'N'
    else:
        return 'P'

verificacao_1 = positivo_negativo(-1)
verificacao_2 = positivo_negativo(2)

print(verificacao_1)
print(verificacao_2)
