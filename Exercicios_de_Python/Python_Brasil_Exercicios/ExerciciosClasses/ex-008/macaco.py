class Macaco:
    def __init__(self,nome,estomago:list= []) -> None:
        self._nome =  nome
        self._estomago = estomago

    def comer(self,alimento:str):
        alimento = alimento.strip().upper()
        if alimento.isalpha:
            self._estomago.append(alimento)

    def digerir(self):
        self._estomago.clear()

    def ver_bucho(self):
        print(f'Comida do estomado do macaco {self._nome}: ')
        print(','.join(self._estomago))
    
    def __getattr__(self,attr):
        if hasattr(self._nome,attr):
            return getattr(self._nome,attr)