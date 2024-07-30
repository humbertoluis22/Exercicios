class Pessoa: 
    def __init__(self,nome:str,idade:int,altura:float) -> None:
        self.nome  = nome
        self.idade = idade
        self.altura = altura
    
    def __str__(self) -> str:
        return f'O/A {self.nome} tem {self.idade} anos e {self.altura} de altura'