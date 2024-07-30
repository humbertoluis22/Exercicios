
def exibi_nome_organizados(*args) -> list:
    print(sorted(args))
    
exibi_nome_organizados('humberto','ana','beatriz')

##segunda forma

nomes = sorted([nome for nome in input('digite uma serie de nomes separados por , :').strip().split(',')])
print(nomes)
