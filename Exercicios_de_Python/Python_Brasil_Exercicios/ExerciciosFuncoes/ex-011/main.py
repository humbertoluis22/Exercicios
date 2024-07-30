from meses import * 

def mes_extenso(data:str) -> str:
    """Coloca o mes por extenso 
    Args:
        data (str): data completa 
        ex:
            11/12/21

    Returns:
        str: _description_
    """
    data = data.split('/')
    try:
        return f'{data[0]} / {meses_do_ano[data[1]]} / {data[2]}'
    except Exception:
        print('Data informada inválida')

data = mes_extenso('24/07/2024')
print(data)