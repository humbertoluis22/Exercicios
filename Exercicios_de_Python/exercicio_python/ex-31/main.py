termo = int(input('digite o primeiro termo da progressao: '))
razao = int(input('digite a razao: '))

impressao = termo + (20) * razao

for i in range(termo,impressao ,razao):
    print(i)

