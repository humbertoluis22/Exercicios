sexo = input('Digite seu sexo F-FEMINO | M-MASCULINO : ').upper().strip()
if sexo not in 'MF':
    print('Sexo inválido')
elif sexo == 'M':
    print('MASCULINO')
elif sexo  == 'F':
    print('FEMININO')