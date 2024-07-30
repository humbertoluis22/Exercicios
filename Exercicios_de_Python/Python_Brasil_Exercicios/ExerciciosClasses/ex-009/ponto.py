class Ponto:
    def __init__(self,x = 0 , y = 0 ) -> None:
        self._x = x 
        self._y = y 
    
    def __str__(self) -> str:
        return f'X = {self._x}, Y = {self._y}'