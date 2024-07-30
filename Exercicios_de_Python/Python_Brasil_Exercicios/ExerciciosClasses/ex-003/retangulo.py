class Retangulo:
    def __init__(self,comprimento,largura) -> None:
        self._comprimento = comprimento
        self._largura = largura
    
    def mudar_lados(self,novo_comprimento,nova_largura):
        self._comprimento = novo_comprimento
        self._largura = nova_largura
    
    def retorna_comprimento(self):
        return self._comprimento
    
    def retorna_largura(self):
        return self._largura
    
    def calcular_area(self):
        area = self._comprimento * self._largura
        return area
    
    def calcular_perimetro(self):
        comprimento = self._comprimento
        largura = self._largura
        perimetro = 2 * (comprimento + largura)
        return perimetro