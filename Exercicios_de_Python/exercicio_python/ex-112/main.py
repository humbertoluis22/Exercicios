codigo = """
numero = int(input('digite um numero: '))
def numero_quadrado(numero):
    numero_quadrado = numero**2
    return numero_quadrado

num = numero_quadrado(numero)
print(f'o NUmero {numero} elevado ao quadrado é {num}')
"""

exec(codigo)
