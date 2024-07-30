class Calculadora: 
    def __init__(self,*args) -> None:
        self.numeros = args
        pass

    def soma(self):
        soma = sum(self.numeros)
        return soma


    def subtrair(self):
        for i in range(len(self.numeros) - 1):
            if i == 0:
                subtrair = self.numeros[i] - self.numeros[i + 1]
                continue
            subtrair -= self.numeros[i + 1]
        return subtrair


    def multiplicar(self):
        for i in range(len(self.numeros) - 1):
            if i == 0 :
                mult = self.numeros[i] * self.numeros[i + 1]
                continue
            mult *= self.numeros[i]
        return mult
    

    def divisao(self):
        for i in range(len(self.numeros) - 1):
            if i == 0 :
                div = self.numeros[i] / self.numeros[i + 1]
                continue
            div /= self.numeros[i]
        return div

