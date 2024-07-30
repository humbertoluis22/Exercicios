def imprime_n_esimo(numero:int) -> None:
    for i in range(1,numero+1):
        for y in range(1,i+1):
            if y == i:
                print(i)
            else:
                print(i,end=' ')
    
imprime_n_esimo(15)