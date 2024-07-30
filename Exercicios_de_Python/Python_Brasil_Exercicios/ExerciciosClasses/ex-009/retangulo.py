from ponto import Ponto

class Retangulo:
    def __init__(self,largura,altura,vertice) -> None:
        self._largura = largura
        self._altura = altura
        self._vertice = vertice

    def centro(self):
        centro_x = self._vertice + self._largura / 2
        centro_y = self._vertice + self._altura / 2
        return Ponto(centro_x,centro_y)
    
    def __str__(self):
        return f"Retangulo(Largura={self._largura}, Altura={self._altura}, Vertice Inferior Esquerdo={self._vertice})"
