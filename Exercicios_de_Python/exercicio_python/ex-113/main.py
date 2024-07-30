"""As sequências de escape ANSI são códigos especiais que permitem 
controlar a formatação do texto no console."""

# texto_exemplo = "palavra em negrito"
# teste = f"\033[1m\033[31m\033[3m{texto_exemplo}\033[3m\033[31m\033[0m"
# print(teste)


def transforma_palavra(funcao): 
    def wrraper(*args,**kwargs):
        texto = funcao(*args,**kwargs)
        texto = f"\033[1m\033[31m\033[3m{texto}\033[3m\033[31m\033[0m"
        return texto
    return wrraper



@transforma_palavra
def saudar(texto):
    return f"ola, {texto}"

print(saudar('humberto'))