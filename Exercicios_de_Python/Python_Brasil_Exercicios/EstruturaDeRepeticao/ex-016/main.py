proximo_numero = 0 
while proximo_numero < 500:
    if proximo_numero == 0 :
        numero_atual = 1
        numero_anterior = 0 
      
    proximo_numero = numero_atual + numero_anterior
    print(proximo_numero)
    numero_anterior = numero_atual
    numero_atual = proximo_numero