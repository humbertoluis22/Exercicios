def quadrado_magico(numero:int)->list[list]:
    """Cria uma lista de lista,
    as listas tem a quantidade de linhas e 
    colunas iguais 

    Args:
        numero (int): Precisa ser impar
        pois utilizamos o metodo siames 
        do cubo magico 

    Returns:
        list[list]: linhas e colunas do 
        cubo magico 
    """
    if numero % 2 == 0:
        print("O numero informado precisa ser impar")
        exit()

    quadrado_magico = [[0] * numero for i in range(numero)]

    numero_quadrado = 1
    i, j = 0, numero // 2

    while numero_quadrado <= numero**2:
        quadrado_magico[i][j] = numero_quadrado
        numero_quadrado += 1
        i_novo = (i - 1) % numero
        j_novo = (j + 1) % numero

        if quadrado_magico[i_novo][j_novo] != 0:
            i += 1
        else:
            i = i_novo
            j = j_novo
    return quadrado_magico

def exibir_cubo_magico(cubo_magico: list[list]) -> None:
    for linha in cubo_magico:
        print(" ".join((f"{numero:<5}" for numero in linha)))


novo_quadrado_magico = quadrado_magico(5)
exibir_cubo_magico(novo_quadrado_magico)
