from carro import Carro

carro = Carro(16,30)
print(carro)
tanque = carro.obter_gasolina()
print(tanque)
carro.adicionar_gasolina(10)
print(carro)
carro.andar(16)
print(carro)