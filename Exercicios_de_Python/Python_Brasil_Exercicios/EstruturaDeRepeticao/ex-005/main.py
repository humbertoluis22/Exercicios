a = 80000
b = 200000
contador = 0

while True:
    taxa_crescimento_a = float(input('digite a taxa de crescimento do pais A: '))
    taxa_crescimento_b = float(input('digite a taxa de crescimento do pais B: '))
    crescimento_a = a * taxa_crescimento_a
    crescimento_b  = b * taxa_crescimento_b

    while a < b :
        a += crescimento_a
        b += crescimento_b
        contador +=1
    print(f'Serão necessarios {contador} anos para o pais A se igualar ou passar o B')
    opcao = int(input('Deseja efetuar um novo calculo [1 - sim | 2- Não] :  '))
    if opcao != 1:
        break
