class Televisao:
    def __init__(self,canal,volume = 0 ) -> None:
        self._canal = canal
        self._volume = volume

    def alterar_volume(self,volume):
        if volume >= 0 and volume <= 100:
            self._volume = volume
        
    def alterar_canal(self,canal):
        if canal >= 0 and canal <= 125:
            self._canal = canal
        
    def retorna_volume(self):
        return self._volume
    
    def retorna_canal(self):
        return self._canal

    def __str__(self) -> str:
        descricao = (f'A televisao estao no canal {self._canal}' +
                     f' e com o valume {self._volume}')
        return descricao