import ipaddress

texto = r'C:\Users\Humberto\Desktop\exercicios\Python_Brasil_Exercicios\ExerciciosArquivos\ex-001\endereco_ip.txt'
resultado = r'C:\Users\Humberto\Desktop\exercicios\Python_Brasil_Exercicios\ExerciciosArquivos\ex-001\resultado.txt'
ip_validos = []
ip_invalido = []

with open(texto,'r') as txt:
    enderecos = txt.read().split('\n')

for endereco in enderecos:
    try:
        ipaddress.ip_address(endereco)
        ip_validos.append(endereco)
    except:
        ip_invalido.append(endereco)
        continue
 

with open(resultado,'w',encoding= 'utf_8') as arquivo:
    arquivo.write('[Endereços válidos:]\n')
    for ip in ip_validos:
        arquivo.write(ip +'\n')
    arquivo.write('[Endereços invalidos:]\n')
    for ip in ip_invalido:
        arquivo.write(ip + '\n')    
