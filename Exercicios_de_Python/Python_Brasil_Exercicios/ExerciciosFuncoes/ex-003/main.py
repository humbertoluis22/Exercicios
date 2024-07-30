def soma_3(
        numero1 : float,numero2:float,numero3:float
        ) -> float:
    """Soma os numeros fornecidos

    Args:
        numero (float): numero para soma

    Returns:
        float: A soma dos tres numeros
    """

    soma = numero1+numero2 + numero3
    return soma


resultado = soma_3(32.43,432.54,432.3)
print(resultado)