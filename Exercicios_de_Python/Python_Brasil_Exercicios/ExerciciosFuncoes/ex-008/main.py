def conta_digito(numero: int) -> int:
    """conta a quantidade de digitos de um numero
    inteiro

    Args:
        numero (int): numero para contagem

    Returns:
        int: quantidade de digitos
    """

    qtd_digitos = len(str(numero))
    return qtd_digitos


qtd_digitos = conta_digito(123)
print(f"A quantidade de digitos do numero informado é {qtd_digitos}")
