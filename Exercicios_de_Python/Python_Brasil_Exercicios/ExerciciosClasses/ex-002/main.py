from quadrado import Quadrado

quadrado_1 = Quadrado(10)
tamanho_1 = quadrado_1.retorna_lado()
print(tamanho_1)
area = quadrado_1.calcula_area()
print(area)
quadrado_1.alterar_lado(15)
area_2 = quadrado_1.calcula_area()
print(area_2)