from pessoa import Pessoa

pessoa_1 = Pessoa('Humberto',18,80,1.73)
pessoa_1.crescer(0.20)
altura = pessoa_1.retorna_altura()
print(altura)
pessoa_1.envelhecer(5)
idade = pessoa_1.retorna_idade()
altura = pessoa_1.retorna_altura()
print(altura)
print(idade)
pessoa_1.engordar(10)
peso = pessoa_1.retorna_peso()
print(peso)
pessoa_1.emagrecer(5)
peso = pessoa_1.retorna_peso()
print(peso)