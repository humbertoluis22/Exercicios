while True:
    nome = input('informe seu nome: ')
    if len(nome) < 3:
        continue
    
    idade = int(input('informe a sua idade: '))
    if idade <= 0 or idade > 150:
        continue

    salario  = float(input('informe seu salario '))
    if salario <= 0 :
        continue

    sexo = input('informe o seu sexo M | F : ').strip().lower()
    if sexo not in 'mf':
        continue

    estado_civil = input('estado civil [s , c , v , d] : ')
    if estado_civil  not in 'scvd':
        continue

    break