class Quadrado:
    def __init__(self,tamanho_lado) -> None:
        self._tamanho_lado = tamanho_lado
    
    def alterar_lado(self,tamanho):
        self._tamanho_lado = tamanho
    
    def retorna_lado(self):
        return self._tamanho_lado

    def calcula_area(self):
        tamanho_area = self._tamanho_lado**2
        return tamanho_area