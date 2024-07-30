class Pessoa:
    def __init__(self) -> None:
        """
        Utilizado para gerar construtores
        serve para informar o que vai ser executado com a classe for instanciada
        """
        self.pessoa = ['henrique','caio','geovanna','beatriz','fernanda']
    

    def __str__(self) -> str:
        """
        Utilizado para gerar uma str apos chamarem a classe
        ex:
            a= Pessoa()
            print(a)
        """
        return  f'A classe possui lista de pessoas'
    

    def __getitem__(self,posicao) -> list[str]:
        """
        utilizado para acessar um elemento atraves do indice 
        ex:
            self.pessoa[posicao]
        """
        return self.pessoa[posicao]
    

    def __len__(self) -> int: 
        """
        Utilizado para verificar o tamanho da lista
        criamos um contador  e um laço de repetição infinito 
        colocar um try except 
        e acrescentamos 1 para o i a cada interação do while 
        assim que for acessado um elemonto com o indice fora do tamanho 
        entra no except e para o laço
        """
        x = 0 
        while True:
            try:
                self.pessoa[x]
                x += 1 
            except:
                break
        return x 
    

    def __add__(self,p2):
        """
        Utilizado para adicionar uma lista a outra
        ex:    
            p2= ['maria','socorro']
            a = self.pessoa + p2
        """
        return self.pessoa + p2


    def __mul__ (self,valor):
        """
        Utilizado para realizar multiplicação
        nesse caso multiplica a lista
        """
        return self.pessoa * 3 
    

    def __delitem__(self,indice):
        """
        Utilizado para excluir um elemento da lista
        ex : 
            del p.pessoa[indice]
        """ 
        return self.pessoa[indice]
    
    
    def __reversed__(self):
        """
        Utilizado para retornar a lista ao contrario
        o primeiro -1 é para acessar o ultimo elemento
        o segundo -1 é para ir ate o elemento 0
        e o terceiro -1 é para ir do ultimo ate o primeiro 
        da função range
        """
        return [self.pessoa[i] for i in range(len(self.pessoa)-1,-1,-1)]
    

    def __eq__(self,p2):
        """
        Utilizado para fazer comparação,
        A forma da comparação fica a escolha 
        Nesse caso compara primeiro o tamanho 
        Depois compara cada elemento da lista para saber se é igual
        """
        if len(self.pessoa) == len(p2):
            x = [self.pessoa[i] == p2[i] for i in range(len(self.pessoa))]
            return all(x)
        else:
            return False
        
    def __iter__(self):
        """
            utiliza uma função geradora
            Serve para poder fazer iteração sobre a classe
            ex: 
                for i in range(len(p.pessoa)):
                     print(p[i])
        """
        i = 0
        while i < len(self.pessoa):
            yield self.pessoa[i]
            i+1