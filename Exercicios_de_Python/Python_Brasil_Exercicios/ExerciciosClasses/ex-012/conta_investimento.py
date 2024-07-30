class ContaInvestimento:
    def __init__(self,nome,conta,saldo = 0 ,tx_juros = 10) -> None:
        self._nome = nome
        self._conta = conta
        self._saldo = saldo
        self._tx_juros = tx_juros
    
    def adicione_juros(self):
        juros = self._tx_juros / 100 
        valor_acrescimo = self._saldo * juros
        self._saldo += valor_acrescimo

    def alterar_nome(self,nome):
        self._nome = nome

    def retorna_saldo(self,saldo):
        return self._saldo
    
    def depositar(self,valor):
        self._saldo += valor
    
    def saque(self,valor):
        self._saldo -= valor
    
    def __str__(self) -> str:
        descricao = ( f'O correntista {self._nome} que possui a ' + 
                     f'conta {self._conta} possui o saldo de R$ : {self._saldo:.2f} '+
                     f'com {self._tx_juros} de taxa de juros')
        return descricao
    