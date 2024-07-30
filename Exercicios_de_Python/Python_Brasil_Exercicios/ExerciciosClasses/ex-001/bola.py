class Bola:
        def __init__(self,cor,circunferencia,material) -> None:
                self._cor  = cor
                self._circunferencia =circunferencia
                self._material = material
                
        def mostrar_cor(self):
                print(self._cor)
    
        def alterar_cor(self,cor):
                self._cor = cor
