class Carro:
    def __init__(self,marca,modelo,ano,cor, valor) -> None:
        self.marca  = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor 
        self.valor = valor
    
    def caracteristicas(self):
        print(f'''  
        Marca:{self.marca}
        Modelo:{self.modelo}
        Ano:{self.ano}
        Cor:{self.cor}
        Valor:{self.valor}
        ''')
        