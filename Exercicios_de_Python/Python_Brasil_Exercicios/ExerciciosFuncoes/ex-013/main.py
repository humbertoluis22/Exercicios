def desenha_moldura(linhas=1,colunas=1)->None:
    """Desenha um retangulo 

    Args:
        linhas (int, optional): quantidaed de linhas. Defaults to 1.
        colunas (int, optional): quantidade de colunas . Defaults to 1.
    """
    molds = ['+','-','|']
    for mold in molds:
        for i in range(1,colunas+1):
            for y in range(1,linhas+1):
                if y == linhas:
                    print(mold)
                else:
                    print(mold,end=' ')
        print()

desenha_moldura(20,5 )