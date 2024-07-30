class Tamagushi:
    def  __init__(self,nome,fome,saude,idade) -> None:
        self._nome = nome
        self._fome = fome
        self._saude = saude
        self._idade = idade
    
    def retorna_nome(self):
        return self._nome
    
    def retorna_fome(self):
        return self._fome
    
    def retorna_saude(self):
        return self._saude
    
    def retorna_idade(self):
        return self._idade

    def alterar_nome(self,nome):
        self._nome = nome

    def alterar_fome(self,nivel_fome):
        self._fome = nivel_fome

    def alterar_saude(self,nivel_saude):
        if nivel_saude > 0 and nivel_saude<= 100:
            self._saude = nivel_saude

    def alterar_idade(self,nova_idade):
        if nova_idade > 0: 
            self._idade = nova_idade

    def humor(self):
        nivel = self._fome + self._saude
        if nivel >= 0 and nivel <= 50:
            print('estressado')
        elif nivel > 60 and nivel < 90:
            print('Bem humorado')
        elif nivel >=90 and nivel < 150:
            print('Feliz')
        else:
            print('Muito feliz')