class Conversor: 
    def __init__(self) -> None:
        self.palavra = ''

    def letra_maiscula(self,palavra) -> None:
        """transforma todas as letras em maisculo
        """
        self.palavra = palavra.upper()

    def exibi_palavra(self) ->None:
        """exibi a palavra em maisculo no terminal
        """
        print(self.palavra)
    