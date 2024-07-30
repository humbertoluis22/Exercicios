codigo_maior = codigo_menor = 0
maior_acidente = menor_acidente = 0

contador_carros = 0

contador_dois_mil = 0
media_dois_mil = 0

for i in range(1, 5 + 1):
    codigo = int(input(f"Informe o codigo da cidade {i}: "))
    n_veiculos = int(input("informe o numero de veiculos de passeio : "))
    n_acidentes = int(input("Informe o numero de acidentes com vitimas :  "))

    contador_carros += n_veiculos
    indice = n_acidentes / n_veiculos

    if i == 1:
        maior_acidente = menor_acidente = indice
        codigo_maior = codigo_menor = codigo
    else:
        if indice > maior_acidente:
            maior_acidente = indice
            codigo_maior = codigo
        elif indice < menor_acidente:
            menor_acidente = indice
            codigo_menor = codigo

    if n_veiculos <= 2000:
        contador_dois_mil += 1
        media_dois_mil += indice


print(
    f"\nO maior indice de acidentes de transitos é de {maior_acidente:.2f}% e pertence a cidade {codigo_maior}"
)
print(
    f"O menor indice de acidentes de transitos é de {menor_acidente:.2f}% e pertence a cidade {codigo_menor}"
)
print(f"Media de veiculos nas 5 cidades é de {(contador_carros/5):.2f}")
print(
    f"A media de acidente nas cidades com menos de 2000 carros é de {(media_dois_mil / contador_dois_mil):.2f}%\n"
)
