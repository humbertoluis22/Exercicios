for i in range(1, 100+1):
    if  i == 1:
        numero_atual = i
        numero_passado = 0 
    soma = numero_passado + numero_atual
    print(soma)
    numero_passado = numero_atual
    numero_atual = soma

  