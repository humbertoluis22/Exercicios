import re 

def verificacao_url(url:str)->bool:
    """verifica se uma url esta correto
    padrao correto:
    inicia com : www.
    termina com: .com.br

    Parameters
    ----------
    url : 
        _description_

    Returns
    -------
    bool
        _description_
    """
    url = url.lower()
    regex = r'^\w{3}..*?.com.br$'
    correto = re.findall(regex,url)
    if correto:
        return True
    else:
        return False
    

url_correta =  'www.exemplo_certo.Com.br'
url_errada = 'www.exemplo_errado.com'
resultado = verificacao_url(url_errada)
if resultado:
    print('url correta')
else:
    print('url errada ')