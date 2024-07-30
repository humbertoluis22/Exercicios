from meses import *

print("Digite sua data de nascimento no modelo :")
dt_nascimento = input("[xx/xx/xxxx] : ").split('/')
try:
    dt_nascimento_extenso = (
        f"{dt_nascimento[0]}/{meses_do_ano[dt_nascimento[1]]}/{dt_nascimento[2]}"
    )
except Exception:
    print('A data infomada esta inválida')

print()
print(dt_nascimento_extenso)