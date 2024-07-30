arquivo = r"C:\Users\Humberto\Desktop\exercicios\Python_Brasil_Exercicios\ExerciciosArquivos\ex-002\usuarios.txt"
usuarios = []
bytes = []
mbs = []
soma_mb = 0

with open(arquivo, "r", encoding="utf-8") as txt:
    conteudo = txt.read().split("\n")
    for linha in conteudo:
        usuario_byte = linha.split()
        usuarios.append(usuario_byte[0])
        bytes.append(usuario_byte[1])


for byte in bytes:
    mb = float(byte) / (1024 * 1024)
    mbs.append(mb)
    soma_mb += mb

usuario_mb = zip(usuarios, mbs)

relatorio = r"C:\Users\Humberto\Desktop\exercicios\Python_Brasil_Exercicios\ExerciciosArquivos\ex-002\relatório.txt"

with open(relatorio, "w", encoding="utf-8") as arquivo:
    arquivo.write('ACME Inc.               Uso do espaço em disco pelos usuários\n')
    arquivo.write('------------------------------------------------------------------------\n')
    arquivo.write('Nr.  Usuário        Espaço utilizado     % do uso\n')
    cont = 1
    for usuario,mb in usuario_mb:
        mb= float(mb)
        arquivo.write(f'{cont} - {usuario:<15} {mb:.2f} {'MB':<15} {((mb/soma_mb)*100):.2f}%\n')
        cont += 1
    arquivo.write(f'Espaço total ocupado: {soma_mb:.2f} MB\n')
    arquivo.write(f'Espaço médio  ocupado: {(soma_mb/(cont -1 )):.2f} MB\n')

