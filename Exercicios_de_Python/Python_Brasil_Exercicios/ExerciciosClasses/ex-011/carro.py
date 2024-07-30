class Carro:
    def __init__(self,consumo, combustivel = 0 ) -> None:
        self._consumo = consumo 
        self._combustivel= combustivel
        
    def obter_gasolina(self):
        return self._combustivel

    def adicionar_gasolina(self,qtd_gasolina):
        if qtd_gasolina > 0:
            self._combustivel += qtd_gasolina

    def andar(self,qtd_km):
        qtd_km_tanque = self._consumo * self._combustivel
        if qtd_km >= 1 and qtd_km <= qtd_km_tanque:
            litros_gastos = (qtd_km_tanque -qtd_km) / self._combustivel
            self._combustivel -= litros_gastos
            
    def __str__(self) -> str:
        descricao = (f'O  carro tem o consumo de {self._consumo} '+
        f'km por litro e ta com {self._combustivel} litros no tanque')
        return descricao