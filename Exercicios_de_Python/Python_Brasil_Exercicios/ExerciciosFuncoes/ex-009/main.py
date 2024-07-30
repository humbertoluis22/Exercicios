def  numero_reverso (numero:int) -> int:
    """Inverte os digitos do numero 

    Args:
        numero (int): numero a ser invertido

    Returns:
        int: numero invertido
    """
    numero_novo = ''
    numero = str(numero)
    for i in range(1,len(numero)+1):
        numero_novo+= numero[-i]
    
    return int(numero_novo)

numero_invertido = numero_reverso(321)
print(f'Número invertido => {numero_invertido}')