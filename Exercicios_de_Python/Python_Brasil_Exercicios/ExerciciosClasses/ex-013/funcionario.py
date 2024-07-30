class Funcionario:
    def __init__(self,nome:str,salario:float) -> None:
        self._nome = nome
        self._salario = salario

    def retorna_nome(self):
        return self._nome

    def retorna_salario(self):
        return self._salario
    
    