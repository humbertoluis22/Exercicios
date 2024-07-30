class BombaDeCompustivel:
    def __init__(self, tipo_combustivel,
                valor_litro,
                qtd_combustivel) -> None:
        self._tipo_combustivel = tipo_combustivel
        self._valor_litro = valor_litro
        self._qtd_combustivel = qtd_combustivel
    
    def abastecer_por_valor(self,valor):
        if valor > self._valor_litro:
            qtd_litro_valor = valor / self._valor_litro
            self._qtd_combustivel -= qtd_litro_valor
            descricao = (f'Foram abastecidos' +
                         f'{(qtd_litro_valor):.2f} litros')
            print(descricao)
        else:
            print('Valor para abastecer insuficiente !!')
    
    def abastecer_por_litro(self,qtd_litro):
        valor_total = qtd_litro * self._valor_litro
        self._qtd_combustivel -= qtd_litro
        descricao = print(f'O valor a ser pago  por {qtd_litro} ' +
            f'litros é de R$:{valor_total:.2f}')
        print(descricao)

    def alterar_valor(self,novo_valor):
        self._valor_litro = novo_valor
    
    def alterar_combustivel(self,combustivel):
        self._tipo_combustivel = combustivel
    
    def alterar_qtd_combustivel(self,qtd_bomba):
        self._qtd_combustivel = qtd_bomba
    
    def __str__(self) -> str:
        descricao = (f'A bomba de {self._tipo_combustivel} '+
        f' possui {self._qtd_combustivel:.2f} litros no tanque e o valor'+
        f' por litro é de R$:{self._valor_litro:.2f}')
        return descricao
