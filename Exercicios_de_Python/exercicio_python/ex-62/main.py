def recebe_qualquer_parametro(*args,**kwargs):
    print(args)
    print(kwargs)

recebe_qualquer_parametro('primeiro args',2332,
                          Nomes = ['humberto','rodrigo','teste'],
                          Idade= [22,34,0])