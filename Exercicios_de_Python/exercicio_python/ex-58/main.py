def soma(numero:int , numero2:int = 5) -> int:
    '''
    default numero2  é 2 
    '''
    return numero + numero2

numero_somado = soma(10)
print(numero_somado)
print()
numero_somado2 = soma(10,15)
print(numero_somado2)