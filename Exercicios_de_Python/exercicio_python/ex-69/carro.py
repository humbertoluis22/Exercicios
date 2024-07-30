class Carro:
    def __init__(self,cor,ano,marca) -> None:
        self.cor = cor 
        self.ano = ano
        self.marca = marca
    
    def informacoes_gerais(self):
        return f'Modelo do carro: {self.marca} | Ano do carro: {self.ano} | Cor do carro : {self.marca} '
    
    