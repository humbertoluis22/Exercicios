class Pessoa:
    def __init__(self,nome,idade,peso,altura) -> None:
        self._nome = nome
        self._idade = idade
        self._peso = peso
        self._altura = altura

    def retorna_nome(self):
        return self._nome.capitalize()
    
    def retorna_idade(self):
        return self._idade
    
    def retorna_peso(self):
        return self._peso

    def retorna_altura(self):
        return self._altura
    
    def envelhecer(self,qtd_anos):
        nova_idade = self._idade + qtd_anos
        if self._idade < 21:
            tempo_crescer = 21 - self._idade 
            cm = tempo_crescer * 0.05
            self._altura += cm
        self._idade = nova_idade
    
    def engordar(self,peso):
        self._peso += peso
    
    def emagrecer(self,peso):
        self._peso -= peso

    def crescer(self,altura):
        self._altura += altura
    