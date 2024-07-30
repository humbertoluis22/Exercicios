lista = ['humberto','joao','lucas']
dicionario = {'idade':[23,54,32],'altura':[1.70,1.67,1.80]}

def multiplos_parametros(*args,**kwargs):
    print(args,kwargs)

multiplos_parametros(*lista,**dicionario)