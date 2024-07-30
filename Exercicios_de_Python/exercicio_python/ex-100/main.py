try: 
    nota = float(input('digite a media doa aluno entre 0 e 1.0 : '))
except:
    print('digite apenas valores numericos!!!!!!')
    exit()

if nota >= 0.6:
    print('aluno aprovado')
else:
    print('aluno reprovado')