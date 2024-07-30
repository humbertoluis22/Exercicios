class ContaCorrente:
    def __init__(self,numero,nome,saldo = 0) -> None:
        self._numero = numero
        self._nome = nome
        self._saldo = saldo
    
    def alterar_nome(self,nome):
        self._nome = nome

    def depositar(self,valor):
        self._saldo += valor
    
    def saque(self,valor):
        self._saldo -= valor
    
    def __str__(self) -> str:
        descricao = ( f'O correntista {self._nome} que possui a ' + 
                     f'conta {self._numero} possui o saldo de R$ : {self._saldo:.2f}')
        return descricao