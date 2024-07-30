from datetime import datetime
import pandas as pd
import os
import os.path
import openpyxl
from pathlib import Path


def padrao_faz_tudo():
#criar um diretorio para salvar os arquivos convertido dentro 
    time = f'{datetime.now(): %d-%m-%y_%H-%M-%S}'
    novo_diretorio = f'meu_novo_diretorio_{time}'
    caminho_novo_diretorio = Path.cwd() /novo_diretorio
    os.makedirs(caminho_novo_diretorio,exist_ok=True)    
    contador  = 0
#pegar todos os arquivos do diretorio atual ok   
    arquivos_do_diretorio_atual = os.listdir(os.getcwd())
    for i in range(len(arquivos_do_diretorio_atual)):
        nome_arquivo,extensao = os.path.splitext(arquivos_do_diretorio_atual[i])
        if extensao == '.csv':
            time = f'{datetime.now(): %d-%m-%y_%H-%M-%S}'
            df = pd.read_csv(arquivos_do_diretorio_atual[i])
            df.to_excel(f'{caminho_novo_diretorio}\\{nome_arquivo}{time}.xlsx')
            contador += contador
        elif contador == 0:
            print('nenhum arquivo com a extensao necessaria foi encontrado')

def executar():
    padrao_faz_tudo()

   

executar()


# os.mkdir(path, mode=0o777, *, dir_fd=None)
#
