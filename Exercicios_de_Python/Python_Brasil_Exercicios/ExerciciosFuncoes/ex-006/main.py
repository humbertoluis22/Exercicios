from horas import * 

def converte_horario(horas:str)-> str:
    """ converte a notação de 24 horas para a notação de 12 horas

    Args:
        horas (str): horario em 24h apenas com horas e minutos seprados
        por ':'
        ex => 12:30

    Returns:
        str: horario em 12h 
    """

    hora_minuto = horas.split(':')
   
    hora = int(hora_minuto[0])
    info = ''
    if hora >= 12 and hora <= 23:
        info = 'P'
        return f'{hora_24_12[hora_minuto[0]]}:{hora_minuto[1]} {info}'
    else:
        info = 'A'
        return f'{hora_minuto[0]}:{hora_minuto[1]} {info}'


def apresetacao_horario()-> None:
    print('Conversor de horas !!')
    while True:
        print('Informe um horario  com hora:minuto [ex : 13:40] ')
        hora = input("horario : ")
        hora_convertida = converte_horario(hora)
        print(f'\nHora convertida : {hora_convertida}\n')
        print('Deseja usar o sistema novamente ? ')
        opcao = input('[1- sim | 2 - não ]: ')
        if opcao == '2':
            print('Tchau Tchau !! :P')
            break
    

apresetacao_horario()