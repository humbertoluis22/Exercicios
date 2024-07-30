from retangulo import Retangulo

comprimento = float(input("Digite o  comprimento do triangulo : "))
largura = float(input("Digite a largura do triangulo : "))

retangulo = Retangulo(comprimento,largura)
comprimento_obj = retangulo.retorna_comprimento()
largura_obj = retangulo.retorna_largura()
area = retangulo.calcular_area()
perimetro = retangulo.calcular_perimetro()
 
print(f'Tamanho da area do triangulo : {area}')
print(f'Tamanho do perimetro do triangulo : {perimetro}')
print(f'Tamanho do comprimento : {comprimento_obj}')
print(f'Tamanho da largura : {largura_obj}')